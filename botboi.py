

import discord
from discord.ext import commands
from discord.ext.commands import Bot
#from key import (username,token)
import asyncio
#import chalk
from boto.s3.connection import S3Connection



bot = commands.Bot(command_prefix='!')
#some guides use client instead of bot

@bot.event
async def on_ready():
    print ("Ready when you are xd")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: pong")
    print ("user has pinged")

@bot.command(pass_context=True)
async def source(ctx):
    await bot.say("https://github.com/androidorb424/Bot_Boi")


@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The users name is: {}".format(user.name))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.status))
    await bot.say("The users highest role is: {}".format(user.top_role))
    await bot.say("The user joined at: {}".format(user.joined_at))

#@bot.command(pass_context=True)
#async def kick(ctx, user: discord.Member):
#    await bot.say("adios(spanish for goodbye), {}. Nerd".format(user.name))
#    await bot.kick(user)


@bot.command(pass_context=True)
async def clear(ctx, amount=10):
    channel = ctx.message.channel
    messages = []
    async for message in bot.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await bot.delete_messages(messages)
    await bot.say('Messages deleted.')



token = S3Connection(os.environ['key'], os.environ['key'])
