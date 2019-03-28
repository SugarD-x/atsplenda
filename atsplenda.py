# Work with Python 3.6
import discord
import random
import asyncio

TOKEN = 'token'

client = discord.Client()

@client.event

#async def on_member_join(self, member):
#        guild = member.guild
#        if guild.system_channel is not None:
#            to_send = 'hey look, a person'.format(member, guild)
#            await guild.system_channel.send(to_send)


async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if "@splenda" in message.content.lower():
        msg = '{0.author.mention} mentioned you splenda. <@385933420389335061>'.format(message)
        print('{0.author.mention} @splendad')
        await message.channel.send(msg)

    if "@spnexa" in message.content.lower():
        msg = 'you wish'.format(message)
        print('someone spnexad')
        await message.channel.send(msg)

    if message.content.startswith('bitch'):
        msg = 'LASAGNA!!!'.format(message)
        print('you india you lose')
        await message.channel.send(msg)

    if message.content.startswith(':))))'):
        msg = 'Woah, calm yo tits there. no one has that many chins'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('XD'):
        msg = 'lulz'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('D:'):
        msg = 'shocking'.format(message)
        #await client.send_message(message.channel, msg)
        await message.channel.send(msg)

    if message.content.startswith('!deleteme'):
       await message.channel.send('I will delete myself now...', delete_after=3.0)

#    if message.content.startswith('advertise'):
#        print('ad')
#       await client.send_file(message.channel, boobs.jpg)

@client.event
async def on_ready():
    game = discord.Game("Minecraft, but for Bots")
    await client.change_presence(status=discord.Status.idle, activity=game)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
