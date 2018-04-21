import random
import asyncio
import aiohttp
import os
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("#","!")
TOKEN = "NDM1NTUwOTA3NjYxNDE4NDk2.DbanQQ.PWbFUAbGyE_odzG9ibK_xL-H-wk"  # Get at discordapp.com/developers/applications/me

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball', 'bolaoito'],
                pass_context=True)

async def eight_ball(context):
    possible_responses = [

    'It is certain',
    'It is decidedly so',
    'Without a doubt',
    'Yes definitely',
    'You may rely on it',
    
    'As I see it, yes',
    'Most likely',
    'Outlook good',
    'Yes',
    'Signs point to yes',
    
    'Reply hazy try again',
    'Ask again later',
    'Better not tell you now',
    'Cannot predict now',
    'Concentrate and ask again'

    

    "Don't count on it",
    'My reply is no',
    'My sources say no',
    'Outlook not so good',
    'Very doubtful' 
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@client.command(name = 'Falou merda',
                description = 'Conta quantas vezes o Billy falou merda',
                brief = 'Billy',
                aliases =['bilou',],
                pass_context = True)
async def falou_merda(context):
    possible_responses = [
    'Caralho Billy para de falar merda',
    'Cala a porra da boca Billy',
    'Meu deus do ceu',
    ''
    ]
    with open(r'bilou.txt','r+') as f:
        value = int(f.read())
        f.seek(0)
        f.write(str(value + 1))
        c = f.read()
        await client.say("O Billy ja falou merda " + str(value) + ' vezes. ' + random.choice(possible_responses))
        f.close()

@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="testando"))
    print("Logged in as " + client.user.name)


@client.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.json(content_type='application/javascript')
        await client.say("Bitconneeeeeeeect price is: $" + response['bpi']['USD']['rate'])



client.run(TOKEN)
