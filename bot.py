import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix="!") #prefix for commands like !remove
blacklist = ["frick", "dang", "darn", "damn", "heck", "crap", "shizzle", "fudge"]

@client.event
async def on_ready():
    print("Bot is alive")
    await client.change_presence(activity=discord.Game(name='Watching for troublemakers')) #fun status of the bot

#purges an amount of messages
@client.command()
async def remove(ctx, amount=0):
    await ctx.channel.purge(limit=amount + 1)
    channel = client.get_channel(810409079481696299)
    await channel.send(str(amount) + " messages were removed.")

#adds a word to the blacklist
@client.command(pass_context=True)
async def addWord(ctx, word):
    blacklist.append(word)
    await ctx.author.send(word + " has been added to the filter.")
    await ctx.message.delete()

#removes a word from the blacklist
@client.command(pass_context=True)
async def delWord(ctx, word):
    blacklist.remove(word)
    await ctx.author.send(word + " has been removed from the filter.")
    await ctx.message.delete()

#sends blacklisted words to user
@client.command(pass_context=True)
async def wordList(ctx):
    await ctx.author.send("The blacklisted words are: " + str(blacklist))

#check to see if one of the blacklisted words is found in a user's message, and if so it will be removed
@client.event
async def on_message(message):
    channel = client.get_channel(810409079481696299)
    author_id = message.author.id
    delKeyword = "!delWord"
    if((author_id != 810408611573661726)):
        for word in blacklist:
            if((word in message.content) and (delKeyword not in message.content)):
                await message.delete()
                await channel.send(getRandomMessage(author_id))
        await client.process_commands(message)

#this function allows the bot to send a snarky reply after a user swears
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

client.run("SECRET TOKEN")
