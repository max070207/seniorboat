import discord
from discord.ext import commands
from discord import utils
from discord.utils import get
import random
from random import randint
import os

TOKEN = 'NzE3NzUzNzIyMjY4MDI0ODMz.Xte6SA.77LAumjtgJatM9SZqaQfW7psFSM' # bot token
prefix = "!"
bot = commands.Bot(command_prefix = prefix)
bot.remove_command("help")
bad_words = ['бля', 'блять', 'пизда', 'хуй', 'ебать', 'пиздец']

POST_ID = 717772627632193537 # post id to read reactions from

#roles list according to emotes
ROLES = {
	'🎮': 713486391279091772, # event role
}

MAX_ROLES_PER_USER = 99999 # max amount of user a roles can have

@bot.event
async def on_ready():
    print('Logged successfully!')
"""
    await bot.change_presence(status = discord.Status.online, activity = discord.Game('!help'))
"""
"""
@bot.event
async def on_member_join(member):
	channel = bot.get_channel(714540713081045063)
	role = discord.utils.get(member.guild.roles, id = 715088242940313630)
	await member.add_roles(role)
	await channel.send(f'Пользователь {member.mention} присоединился к серверу!')

@bot.event
async def on_member_remove(member):
	channel = bot.get_channel(714540713081045063)
	await channel.send(f'Пользователь {member.mention} покинул сервер.')
"""
"""
@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send(f'{ctx.author.name}, такой команды не существует')
"""
"""
@bot.event
async def on_message(message):
	await bot.process_commands(message)
	msg = message.content.lower()
	if msg in bad_words:
		await message.delete()
		await message.author.send(f'{message.author.name}, используйте меньше мата, пожалуйста')
"""
@bot.event
async def on_raw_reaction_add(payload):
	channel = bot.get_channel(payload.channel_id) # получаем объект канала
	message = await channel.fetch_message(payload.message_id) # получаем объект сообщения
	member = utils.get(message.guild.members, id=payload.user_id) # получаем объект пользователя который поставил реакцию
 
	try:
		emoji = str(payload.emoji) # эмоджик который выбрал юзер
		role = utils.get(message.guild.roles, id=ROLES[emoji]) # объект выбранной роли (если есть)
 
		await member.add_roles(role)
		print('[SUCCESS] User {0.display_name} has got the {1.name} role'.format(member, role))
 
	except KeyError as e:
		print('[ERROR] KeyError, no role found for ' + emoji)
	except Exception as e:
		print(repr(e))
@bot.event
async def on_raw_reaction_remove(payload):
	channel = bot.get_channel(payload.channel_id) # получаем объект канала
	message = await channel.fetch_message(payload.message_id) # получаем объект сообщения
	member = utils.get(message.guild.members, id=payload.user_id) # получаем объект пользователя который поставил реакцию
 
	try:
		emoji = str(payload.emoji) # эмоджик который выбрал юзер
		role = utils.get(message.guild.roles, id=ROLES[emoji]) # объект выбранной роли (если есть)
 
		await member.remove_roles(role)
		print('[SUCCESS] Role {1.name} was been removed from user {0.display_name}'.format(member, role))
 
	except KeyError as e:
		print('[ERROR] KeyError, no role found for ' + emoji)
	except Exception as e:
		print(repr(e))
"""
Информация:
"""
@bot.command()
async def help(ctx):
    embed=discord.Embed(color=0x91f735)
    embed.set_author(name="Доступные команды:")
    embed.add_field(name="**Помощь:**", value="`!help`, `!info`", inline = False)
    embed.add_field(name="**Модерация:**", value="`!clear`, `!kick`, `!ban`, `!unban`", inline = False)
    embed.add_field(name="**Весёлости:**", value="`!user`, `!question`, `!avatar`, `!say`, `!dm_send`", inline = False)
    await ctx.send(embed=embed)

@bot.command()
async def info(ctx):
    embed=discord.Embed(color=0x91f735)
    embed.set_author(name="Информация:")
    embed.add_field(name="Мой префикс: `!`", value="Пропиши команду `!help` для большей информации.", inline = False)
    embed.add_field(name="Бот создан:", value="03.06.2020", inline = False)
    embed.add_field(name="Мой создатель:", value="IAmLegend#2364",  inline = False)
    await ctx.send(embed=embed)

@bot.command()
async def user(ctx, member: discord.Member):
	embed = discord.Embed(title = 'Основная информация:', colour = discord.Color.green())
	embed.set_author(name = f'Информация о пользователе "{member.name}":', icon_url = member.avatar_url)
	embed.add_field(name = f'Имя: {member.name}', value = f'ID = {member.id}', inline = False)
	embed.add_field(name = f'Был зарегистрирован: {member.created_at}', value = f"Аватар пользователя {member.name}:", inline = False)
	embed.set_image(url='{}'.format(member.avatar_url))
	await ctx.send(embed=embed)

"""
Модерация:
"""
"""
@bot.command()
@commands.has_permissions(administrator = True)
async def mute(ctx, member: discord.Member):
	embed = discord.Embed(title = 'Mute', colour = discord.Color.red())
	await ctx.channel.purge(limit=1)
	mute_role = discord.utils.get(ctx.message.guild.roles, name = 'Mute')
	await member.add_roles(mute_role)
	embed.set_author(name = member.name, icon_url = member.avatar_url)
	embed.add_field(name = 'Mute user', value = 'Muted User : {}'.format(member.mention))
	embed.set_footer(text = 'Был замьючен игроком {}'.format(ctx.author.name), icon_url = ctx.author.avatar_url)
	await ctx.send(embed=embed)
"""

@bot.command()
@commands.has_permissions(administrator = True)
async def kick(ctx, member : discord.Member, *, reason=None):
	embed = discord.Embed(title = 'Kick', colour = discord.Color.red())
	await ctx.channel.purge(limit=1)
	await member.kick(reason=reason)
	embed.set_author(name = member.name, icon_url = member.avatar_url)
	embed.add_field(name = 'Kick user', value = 'Kicked User : {}'.format(member.mention))
	embed.set_footer(text = 'Был кикнут игроком {}'.format(ctx.author.name), icon_url = ctx.author.avatar_url)
	await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator = True)
async def ban(ctx, member : discord.Member, *, reason=None):
	embed = discord.Embed(title = 'Ban', colour = discord.Color.red())
	await ctx.channel.purge(limit=1)
	await member.ban(reason=reason)
	embed.set_author(name = member.name, icon_url = member.avatar_url)
	embed.add_field(name = 'Ban user', value = 'Banned User : {}'.format(member.mention))
	embed.set_footer(text = 'Был забанен игроком {}'.format(ctx.author.name), icon_url = ctx.author.avatar_url)
	await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
	await ctx.channel.purge(limit=1)

	banned_users = await ctx.guild.bans()

	for ban_entry in banned_users:
		user = ban_entry.user

		await ctx.guild.unban(user)
		await ctx.send('User was been unbanned')

		return

@bot.command()
@commands.has_permissions(administrator = True)
async def clear(ctx, amount : int):
	await ctx.channel.purge(limit=amount)
	await ctx.channel.send('Messages was been deleted')
"""
Пользовательские команды:
"""
@bot.command()
async def rules(ctx):
    embed=discord.Embed(color=0x91f735)
    embed.add_field(name=":exclamation:**ПРАВИЛА СЕРВЕРА**:exclamation:", value="`1.`__***Аватарка и никнейм НЕ должны:***__", inline = False)
    embed.add_field(name="`1.1`Нарушать общепринятые моральные и этические нормы.", value="`1.2`Быть оскорбительными в какой-либо форме для участников.", inline = False)
    embed.add_field(name="`1.3`Использовать в никах адреса веб–сайтов, адреса email и прочую контактную информацию.", value="`2.`__***ЗАПРЕЩАЕТСЯ:***__", inline = False)
    embed.add_field(name="`2.1`Оскорблять других пользователей или администрацию сервера.", value="`2.2`Дискриминация по любому признаку — расовому, половому, религиозному и т. д.", inline = False)
    embed.add_field(name="`2.3`Проявление агрессии.", value="`2.4`Злоупотребление матерными выражениями.", inline = False)
    embed.add_field(name="`2.5` Отправлять  приглашения на сторонние сервера Discord.", value="`2.6`Попрошайничество каких либо привилегий. ", inline = False)
    embed.add_field(name="`2.7`Спам упоминаниями и масспингом (everyone и here). ", value="`2.8`Отправка сообщений, содержащих NSFW контент.", inline = False)
    await ctx.send(embed=embed)
"""
Весёлости:
"""
@bot.command()                              
async def avatar(ctx, member: discord.Member):
	embed=discord.Embed(color=0x91f735)
	embed.set_author(name=f"Аватар пользователя {member.name}:")
	embed.set_image(url='{}'.format(member.avatar_url))
	await ctx.send(embed=embed)

@bot.command()
async def say(ctx, *args):
    output = ' '
    for word in args:
        output += word
        output += ' '
    await ctx.send(output)

@bot.command(aliases=['8ball', 'test'])
async def question(ctx, *, question):
	responses = ["Да", 
				 "Нет"
				 "Безусловно"
				 "Ни в коем случае"
				 "Конечно"
				 "Вот ещё"
				 "Ну да"
				 "Ни за что"
				 "Действительно"
				 "Ещё чего"
				 "Точно"
				 "Вовсе нет"
				 "Так точно"
				 "И речи быть не может"
				 "Разумеется"
				 "Никак нет"
				 "Согласен"
				 "Обсуждению не подлежит"]
	await ctx.send(random.choice(responses))


@bot.command()
async def dm_send(ctx, member: discord.Member):
	await member.send(f'{member.name}, привет от {ctx.author.name}')
"""
Работа с голосовыми каналами:
"""
"""
@bot.command()
async def join(ctx):
	global voice
	channel = ctx.message.author.voice.channel
	voice = get(bot.voice_clients, guild = ctx.guild)

	if voice and voice.is_connected():
		await voice.move_to(channel)

	else:
		await channel.connect()
	await ctx.send(f'Бот подсоединился к каналу: {channel}')

@bot.command()
async def leave(ctx):
	channel = ctx.message.author.voice.channel
	voice = get(bot.voice_clients, guild = ctx.guild)

	if voice and voice.is_connected():
		await voice.disconnect()

	else:
		await channel.disconnect()
	await ctx.send(f'Бот покинул канал: {channel}')
"""
"""
Ошибки:
"""
"""
@mute.error
async def mute_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(f'{ctx.author.mention}, укажи пользователя, которого необходимо замьютить')

	if isinstance(error, commands.MissingPermissions):
		await ctx.send(f'{ctx.author.mention}, недостаточно прав для выполнения команды')

@kick.error
async def kick_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(f'{ctx.author.mention}, укажи пользователя, которого необходимо кикнуть')

	if isinstance(error, commands.MissingPermissions):
		await ctx.send(f'{ctx.author.mention}, недостаточно прав для выполнения команды')

@ban.error
async def ban_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(f'{ctx.author.mention}, укажи пользователя, которого необходимо забанить')

	if isinstance(error, commands.MissingPermissions):
		await ctx.send(f'{ctx.author.mention}, недостаточно прав для выполнения команды')

@unban.error
async def unban_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(f'{ctx.author.mention}, укажи пользователя, которого необходимо разбанить')

	if isinstance(error, commands.MissingPermissions):
		await ctx.send(f'{ctx.author.mention}, недостаточно прав для выполнения команды')

@clear.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(f'{ctx.author.mention}, укажи количество сообщений, которые необходимо удалить')

	if isinstance(error, commands.MissingPermissions):
		await ctx.send(f'{ctx.author.mention}, недостаточно прав для выполнения команды')

@dm_send.error
async def dm_send_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(f'{ctx.author.zxL0mention}, укажи пользователя, которому необходимо отправить сообщение')

	if isistance(error, commands.
@say.error
async def say_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(f'{ctx.author.mention}, укажи сообщение, которое необходимо повторить')

@question.error
async def question_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(f'{ctx.author.mention}, задай мне вопрос')

@avatar.error
async def avatar_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(f'{ctx.author.mention},  упомяни участника, аватар которого хочешь увидеть')
"""
# Run
token = os.environ.get('BOT_TOKEN')

bot.run(str(token))
