# Work with Python 3.6
import discord

TOKEN = 'token'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if "@splenda" in message.content.lower():
        msg = '<@385933420389335061>'.format(message)
        await message.channel.send(msg)

    if "@spnexa" in message.content.lower():
        msg = 'you wish'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('bitch'):
        msg = 'lasagna'.format(message)
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



@client.event
async def on_ready():
    game = discord.Game("Minecraft, but for Bots")
    await client.change_presence(status=discord.Status.idle, activity=game)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
