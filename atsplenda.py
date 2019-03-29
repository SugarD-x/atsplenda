import discord
import random
import asyncio

TOKEN = 'token'

client = discord.Client()

@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if str(channel) == "general":
            await client.send_message(f"hey look, a person")

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if "@splenda" in message.content.lower():
        msg = '{0.author.mention} mentioned you, splenda. <@385933420389335061>'.format(message)
        #logmsg = '${member.user.tag} splendad'
        print(msg)
        await message.channel.send(msg)

    if message.content.startswith('anon @splenda'):
        msg = 'you were anonymously @ed splenda. <@385933420389335061>'.format(message)
        print('anonsplenda')
        channel = client.get_channel(510536109990871051)
        await channel.send(msg)

    if "@spnexa" in message.content.lower():
        msg = 'you wish'.format(message)
#        logmsg = '${member.user.tag} spnexad'.format(message)
        print('someone spnexad')
        await message.channel.send(msg)

    if message.content.startswith(':('):
        msg = 'cheer up. theres no need to be sad. the world is a wonderful place. i mean, it kinda sucks here. but its as wonderful as you make it. so make it wonderful'.format(message)
        print('cheerup')
        await message.channel.send(msg)

    if message.content.startswith('bitch'):
        msg = 'LASAGNA!!!'.format(message)
        print('you india you lose')
        await message.channel.send(msg)

    if message.content.startswith(':)))'):
        msg = 'Woah, calm yo tits there. no one has that many chins'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('XD'):
        msg = 'lulz'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('ooof'):
        msg = 'no, just no'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('D:'):
        msg = 'shocking'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('!deleteme'):
        await message.channel.send('I will delete myself now...', delete_after=3.0)

    if  "<@560446299040645122>" in message.content.lower():
        msg = 'ima bot. beep boop. did you mean @splenda?'.format(message)
        print('boop beep')
        await message.channel.send(msg)

    if  "its quiet" in message.content.lower():
        msg = 'https://tenor.com/view/antisocial-hide-meme-introvert-gif-9201075'.format(message)
        print('quiet')
        await message.channel.send(msg)

    if "polygraph" in message.content.lower():
        await message.channel.send('lie detectors are a lie', file=discord.File('lie-behind-the-lie-detector.pdf'))

    if "getoptifine" in message.content.lower():
        await message.channel.send('here ya go', file=discord.File('optifine.jar'))

    if message.content.startswith('advertise'):
        print('ad')
        await message.channel.send('THIS IS AN ADVERTISEMENT', file=discord.File('boobs.jpg'))

@client.event
async def on_ready():
    game = discord.Game("Minecraft, but for Bots")
    await client.change_presence(status=discord.Status.idle, activity=game)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
