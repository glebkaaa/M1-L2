import discord
from discord.ext import commands
from random import choice

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')


@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send('he' * count_heh)

# мой код доработки


@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)


@bot.command()
async def choose(ctx, choices: str):
    await ctx.send(choice(choices))


@bot.command()
async def cool(ctx):
    possible = ['cool', 'bad']
    await ctx.send(f'The bot is {choice(possible)}')

bot.run('token')
