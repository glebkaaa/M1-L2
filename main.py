import discord
from discord.ext import commands
from random import choice
from math import hypot, pow
from credits import bot_token

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')


@bot.command()
async def show(ctx):  # использую такое название, потому что help занято
    await ctx.send('Привет, вот что я умею: ' + '\n' + '$hello - приветствие' + '\n' + '$show - возможности бота' + '\n' + '$degree - возведение произвольного числа в степень' + '\n' + '$hypot - возвращает евклидова число' + '\n' + '$plus - складывает 2 числа' + '\n' + '$choose - возвращает случайную букву из слова или предложения' + '\n' + '$cool - случайная реакция бота')


@bot.command()
async def degree(ctx, number: int, count: int):
    if count >= 0:
        await ctx.send(int(pow(number, count)))
    elif count < 0:
        await ctx.send('Пока, я не научился такому :(' + '\n' + f'Пример, {number} в кубе:') # Команда pow хорошо с этим справляется. Сделано исключительно для разнообразия.
        await ctx.send(int(pow(number, 3)))


@bot.command()
async def hypot(ctx, number: int, number2: int):
    await ctx.send(hypot(number, number2))


@bot.command()
async def plus(ctx, left: int, right: int):
    await ctx.send(left + right)


@bot.command()
async def choose(ctx, choices: str):
    await ctx.send(choice(choices))


@bot.command()
async def cool(ctx):
    possible = ['cool', 'bad', 'awesome', 'incredible', 'awful', 'so-so']
    await ctx.send(f'The bot is {choice(possible)}')


bot.run(bot_token)
