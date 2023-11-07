import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.command()
async def chat(ctx, *, message):
    if message:
        await ctx.send(message)

bot.run('MTE3MDcyODk4ODkyMzE0MjIxNg.GUD4-M.REbqXKkwJBzoZeg_bcu6Z7F1ZWq_m2HiLfvZAs')
