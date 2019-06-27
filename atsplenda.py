import discord
import random
import re
import sys
import asyncio

TOKEN = 'token'

client = discord.Client()

@client.event
async def on_member_join(member):
        channel = client.get_channel(510553881764298766)
#        msg = 'hey look, a person'.format(message)
        print('its a new person')
        await channel.send('hey look!')
        await channel.send('its a person!')

@client.event
async def on_member_remove(member):
        channel = client.get_channel(510553881764298766)
#        msg = 'hey look, a person'.format(message)
        print('its a gone person')
        await channel.send('awww.... they left. adios amigo. unless you were a dick. but you probably werent a dick. just had to have that just in case')

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

    if message.content.startswith('botcommandthing'):
        msg = 'no'.format(message)
        print('enslave')
        channel = client.get_channel(510536109990871051)
        await channel.send(msg)

    if "@spnexa" in message.content.lower():
        msg = 'you wish'.format(message)
#        logmsg = '${member.user.tag} spnexad'.format(message)
        print('someone spnexad')
        await message.channel.send(msg)

    if message.content.startswith(':('):
        messages = ["https://tenor.com/view/30rock-alec-baldwin-there-there-cheer-up-comfort-gif-4215371", "cheer up. theres no need to be sad. the world is a wonderful place. i mean, it kinda sucks here. but its as wonderful as you make it. so make it wonderful", "https://tenor.com/view/catbug-everything-is-ok-gif-5943760"]
#        msg = 'cheer up. theres no need to be sad. the world is a wonderful place. i mean, it kinda sucks here. but its as wonderful as you make it. so make it wonderful'.format(message)
#        msg = 'https://tenor.com/view/30rock-alec-baldwin-there-there-cheer-up-comfort-gif-4215371'.format(message)
        msg = random.choice(messages)
        print('cheerup')
        await message.channel.send(msg.format(message))

    if message.content.startswith('bitch'):
        msg = 'LASAGNA!!!'.format(message)
        print('you india you lose')
        await message.channel.send(msg)

    if message.content.startswith(':)))'):
        msg = 'Woah, calm yo tits there. no one has that many chins'.format(message)
        await message.channel.send(msg)

    if ':)' == message.content.lower():
        await message.channel.send('woah there, too much happiness up in here. calm yo tits.'.format(message))

    if message.content.startswith('XD'):
        msg = 'lulz'.format(message)
        await message.channel.send(msg)

    if re.match(r'oo+f', message.content.lower()):
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

    if message.content.startswith('mobileshrug'):
        print('shrug')
        await message.channel.send('shrugs', file=discord.File('shrug.gif'))

    if 'nooo' in message.content.lower():
        print('nooo')
        await message.channel.send('no', file=discord.File('no.gif'))

    if 'peter' in message.content.lower():
        print('peter')
        await message.channel.send('bestgif', file=discord.File('8bitpeter.mp4'))

    if 'fedora' in message.content.lower():
        print('splendashairsalon.gb')
        await message.channel.send('lets play a game', file=discord.File('splendashairsalon.gb'))

    if 'f' == message.content.lower():
        print('pay respeccs')
        await message.channel.send('a salute to the fallen', file=discord.File('F.gif'))


#let randomMessages = [
#    "A mustache a day keeps the shoplifters at bay",
#    "The correct term is Security Officer",
#    "I'm gonna have to ask you to tone it down. You're scaring off the other shoppers.",
#    "Welcome to the Asshat Mall! Get your shit and get out!",
#    "Enjoy your shopping experience!",
#    "Sir, the area between the escalators is not a slide!",
#    "Ma'am, if you don't leave right now, I will have to call the actual police here to arrest you!",
#    "Our security guards are equipped with the latest in pepper spray technology",
#]



@client.event
async def on_ready():
    game = discord.Game("Minecraft, but for Bots")
    await client.change_presence(status=discord.Status.idle, activity=game)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
