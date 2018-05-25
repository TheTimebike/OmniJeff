import discord
client = discord.Client()
dictTest = {}
@client.event
async def on_message(message):
    if message.content.lower().startswith('!omnijeff test'):
        emoteList, scoreList = open('{0.name}/EmoteList{0.id}.txt'.format(message.channel.server), 'r').readlines(), open('{0.name}/ScoreList{0.id}.txt'.format(message.channel.server), 'r').readlines()
        for emote in emoteList:
            dictTest[emote.rstrip()] = str(scoreList[emoteList.index(emote)]).rstrip()
        for item, value in dictTest.items():
            print('{0} has a value of {1}'.format(item, value))
client.run(open('./Token.txt', 'r').readlines()[0])
