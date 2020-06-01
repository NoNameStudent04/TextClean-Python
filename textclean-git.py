import discord, asyncio, time, datetime
from discord.ext import commands
from discord.ext.commands import Bot

client = commands.Bot(command_prefix ='tc/')
client.remove_command("help")
token = 'Bot Token Here'

@client.event
async def on_ready():
    print("봇 ID : " + str(client.user.id))
    print("봇 이름 : " + str(client.user.name))
    game = discord.Game("WA SANS PPAP")
    await client.change_presence(status=discord.Status.idle, activity=game)

@client.command(pass_context=True)
async def clean(ctx):
    await ctx.channel.purge(limit=999999999999999999999999999)
    await ctx.channel.purge(limit=999999999999999999999999999)
    await ctx.channel.purge(limit=999999999999999999999999999)
    await ctx.channel.purge(limit=999999999999999999999999999)
    await ctx.channel.purge(limit=999999999999999999999999999)
    embed = discord.Embed(
            title=":wink: Success!",
            description="All messages on that channel have been successfully cleared.",
            color=0xFFFFFF,
            timestamp=datetime.datetime.utcnow()
        )
    await ctx.send(embed=embed)

client.run(token)