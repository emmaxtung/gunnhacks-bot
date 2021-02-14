import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Bot is alive")
    await client.change_presence(activity=discord.Game(name='Watching for troublemakers'))

@client.command()
async def remove(ctx, amount=0):
    await ctx.channel.purge(limit=amount + 1)
    channel = client.get_channel(810409079481696299)
    await channel.send(str(amount) + " messages were removed.")

client.run("DISCORD_TOKEN")
