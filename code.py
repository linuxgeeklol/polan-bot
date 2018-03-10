import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
bot = commands.Bot(command_prefix='plox ')

@bot.event
async def on_ready():
    print ("Ready when you are xd")
    print ("I am running on " + bot.user.name)
    print ("Pierogi to the resuce!")
    print ("bork bork")


@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("Polan can into ping! :flag_pl:")

@bot.command(pass_context=True)
async def cube(ctx, user:discord.Member):
    embed.add_field(value="{} is officially a cube according to Jewish physics. Oy vey.".format(user.name))
    await bot.say(embed=embed) 


bot.run(token)
