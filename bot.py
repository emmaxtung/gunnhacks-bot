import discord
import random
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
    blacklist = ["frick", "dang", "darn", "damn", "heck", "crap", "shizzle", "fudge"]
    channel = client.get_channel(810409079481696299)
    author_id = message.author.id
    for word in blacklist:
        if(word in message.content):
            await message.delete()
            await channel.send(getRandomMessage(author_id))
    await client.process_commands(message)

def getRandomMessage(user_id):
    user_id = '<@' + str(user_id) + '>'
    responses = [
        "{} is having a bad day.. poor thing.",
        "{} woke up and chose violence today.",
        "{}, was that really necessary?",
        "{} thinks everyone  here is really amazing!",
        "I heard soap was one of {}'s favorite things to eat!",
        "Keep it PG, {}."
    ]
    reply = random.choice(responses)
    reply = reply.format(user_id)

    return reply

client.run("ODEwNDA4NjExNTczNjYxNzI2.YCjN1Q.Nk_OTLEMYcew_NQubaLFkiCS4Tk")
