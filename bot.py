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

@client.event
async def on_message(message):
    blacklist = ["frick", "frickers", "motherfrickers", "motherfrick", "dang", "darn", "damn", "heck", "crap", "shizzle", "fudge"]
    for word in blacklist:
        if(word in message.content):
            await message.delete()
    await client.process_commands(message)

client.run("SECRET TOKEN")
