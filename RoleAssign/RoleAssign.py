import discord
import asyncio
client = discord.Client()
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print(discord.__version__)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('$test'):
        msg = await message.channel.send('Platform')
        await msg.remove_reaction('xbox:424735397214421004')
        await msg.remove_reaction('ps4:424735418219757568')
        await msg.remove_reaction('bnet:424735377106927616')
        await msg.remove_reaction('trash:431931243181899777')

@client.event
async def on_raw_reaction_add(payload):
    try:
        if 'admin' in [y.name.lower() for y in client.get_guild(payload.guild_id).get_member(payload.user_id).roles] or 'moderator' in [y.name.lower() for y in client.get_guild(payload.guild_id).get_member(payload.user_id).roles]:
            return
        if payload.channel_id != #RoleAssign channel:
            return
        msg = await client.get_channel(payload.channel_id).get_message(payload.message_id)
        print(client.get_guild(payload.guild_id).get_member(payload.user_id).display_name)
        print(payload.emoji)
        print('---------------------')
        for role in client.get_guild(payload.guild_id).roles:
            if role.name == 'Europe':
                euRole = role
            if role.name == 'Americas':
                naRole = role
            if role.name == 'Asia':
                asRole = role            
        if payload.message_id == #Region message id:
            if str(payload.emoji) == '<:na:424709351471710223>':
                while True:
                    if "americas" not in [y.name.lower() for y in client.get_guild(payload.guild_id).get_member(payload.user_id).roles]:
                        await client.get_guild(payload.guild_id).get_member(payload.user_id).add_roles(naRole)
                    elif "americas" in [y.name.lower() for y in client.get_guild(payload.guild_id).get_member(payload.user_id).roles]:
                            break
                while True:
                    if "europe" in [y.name.lower() for y in client.get_guild(payload.guild_id).get_member(payload.user_id).roles]:
                        await client.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(euRole)
                    elif "europe" not in [y.name.lower() for y in client.get_guild(payload.guild_id).get_member(payload.user_id).roles]:
                        break
                while True:
                    if "asia" in [y.name.lower() for y in client.get_guild(payload.guild_id).get_member(payload.user_id).roles]:
                        await client.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(asRole)
                    elif "asia" not in [y.name.lower() for y in client.get_guild(payload.guild_id).get_member(payload.user_id).roles]:
                        break 
                await msg.remove_reaction('trash:431931243181899777', client.get_guild(payload.guild_id).get_member(payload.user_id))
                await msg.remove_reaction('Asia:424709328914743317', client.get_guild(payload.guild_id).get_member(payload.user_id))
                await msg.remove_reaction('eu:424709340281307136', client.get_guild(payload.guild_id).get_member(payload.user_id))                    
            elif str(payload.emoji) == '<:eu:424709340281307136>':
                while True:
                    if "europe" not in [y.name.lower() for y in client.get_guild(payload.guild_id).get_member(payload.user_id).roles]:
                        await client.get_guild(payload.guild_id).get_member(payload.user_id).add_roles(euRole)
                    elif "europe" in [y.name.lower() for y in client.get_guild(payload.guild_id).get_member(payload.user_id).roles]:
                            break
                while True:
                    if "americas" in [y.name.lower() for y in client.get_guild(payload.guild_id).get_member(payload.user_id).roles]:
                        await client.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(naRole)
                    elif "americas" not in [y.name.lower() for y in client.get_guild(payload.guild_id).get_member(payload.user_id).roles]:
                        break
                while True:
                    if "asia" in [y.name.lower() for y in client.get_guild(payload.guild_id).get_member(payload.user_id).roles]:
                        await client.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(asRole)
                    elif "asia" not in [y.name.lower() for y in client.get_guild(payload.guild_id).get_member(payload.user_id).roles]:
                        break  
                await msg.remove_reaction('trash:431931243181899777', client.get_guild(payload.guild_id).get_member(payload.user_id))
                await msg.remove_reaction('Asia:424709328914743317', client.get_guild(payload.guild_id).get_member(payload.user_id))
                await msg.remove_reaction('na:424709351471710223', client.get_guild(payload.guild_id).get_member(payload.user_id))                                                           
            elif str(payload.emoji) == '<:Asia:424709328914743317>':
                while True:
                    if "asia" not in [y.name.lower() for y in client.get_guild(payload.guild_id).get_member(payload.user_id).roles]:
                        await client.get_guild(payload.guild_id).get_member(payload.user_id).add_roles(asRole)
                    elif "asia" in [y.name.lower() for y in client.get_guild(payload.guild_id).get_member(payload.user_id).roles]:
                            break
                while True:
                    if "americas" in [y.name.lower() for y in client.get_guild(payload.guild_id).get_member(payload.user_id).roles]:
                        await client.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(naRole)
                    elif "americas" not in [y.name.lower() for y in client.get_guild(payload.guild_id).get_member(payload.user_id).roles]:
                        break
                while True:
                    if "europe" in [y.name.lower() for y in client.get_guild(payload.guild_id).get_member(payload.user_id).roles]:
                        await client.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(euRole)
                    elif "europe" not in [y.name.lower() for y in client.get_guild(payload.guild_id).get_member(payload.user_id).roles]:
                        break
                await msg.remove_reaction('trash:431931243181899777', client.get_guild(payload.guild_id).get_member(payload.user_id))
                await msg.remove_reaction('na:424709351471710223', client.get_guild(payload.guild_id).get_member(payload.user_id))
                await msg.remove_reaction('eu:424709340281307136', client.get_guild(payload.guild_id).get_member(payload.user_id))                      
            elif str(payload.emoji) == '<:trash:431931243181899777>':
                while True:
                    if "americas" in [y.name.lower() for y in client.get_guild(payload.guild_id).get_member(payload.user_id).roles]:
                        await client.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(naRole)
                    elif "americas" not in [y.name.lower() for y in client.get_guild(payload.guild_id).get_member(payload.user_id).roles]:
                        break
                while True:
                    if "europe" in [y.name.lower() for y in client.get_guild(payload.guild_id).get_member(payload.user_id).roles]:
                        await client.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(euRole)
                    elif "europe" not in [y.name.lower() for y in client.get_guild(payload.guild_id).get_member(payload.user_id).roles]:
                        break
                while True:
                    if "asia" in [y.name.lower() for y in client.get_guild(payload.guild_id).get_member(payload.user_id).roles]:
                        await client.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(asRole)
                    elif "asia" not in [y.name.lower() for y in client.get_guild(payload.guild_id).get_member(payload.user_id).roles]:
                        break
                await msg.remove_reaction('trash:431931243181899777', client.get_guild(payload.guild_id).get_member(payload.user_id))
                await msg.remove_reaction('Asia:424709328914743317', client.get_guild(payload.guild_id).get_member(payload.user_id))
                await msg.remove_reaction('na:424709351471710223', client.get_guild(payload.guild_id).get_member(payload.user_id))
                await msg.remove_reaction('eu:424709340281307136', client.get_guild(payload.guild_id).get_member(payload.user_id))                      
        elif payload.message_id == #Platform message ID:
            if str(payload.emoji) == '<:xbox:424735397214421004>' and '[XB]' not in client.get_guild(payload.guild_id).get_member(payload.user_id).display_name and len(client.get_guild(payload.guild_id).get_member(payload.user_id).display_name) < 28:
                await client.get_guild(payload.guild_id).get_member(payload.user_id).edit(nick=str(client.get_guild(payload.guild_id).get_member(payload.user_id).display_name) + ' [XB]')
                await msg.remove_reaction('ps4:424735418219757568', client.get_guild(payload.guild_id).get_member(payload.user_id))
                await msg.remove_reaction('bnet:424735377106927616', client.get_guild(payload.guild_id).get_member(payload.user_id))
                await msg.remove_reaction('trash:431931243181899777', client.get_guild(payload.guild_id).get_member(payload.user_id))
            elif str(payload.emoji) == '<:ps4:424735418219757568>' and '[PS]' not in client.get_guild(payload.guild_id).get_member(payload.user_id).display_name and len(client.get_guild(payload.guild_id).get_member(payload.user_id).display_name) < 28:
                await client.get_guild(payload.guild_id).get_member(payload.user_id).edit(nick=str(client.get_guild(payload.guild_id).get_member(payload.user_id).display_name) + ' [PS]')
                await msg.remove_reaction('xbox:424735397214421004', client.get_guild(payload.guild_id).get_member(payload.user_id))
                await msg.remove_reaction('bnet:424735377106927616', client.get_guild(payload.guild_id).get_member(payload.user_id))
                await msg.remove_reaction('trash:431931243181899777', client.get_guild(payload.guild_id).get_member(payload.user_id))
            elif str(payload.emoji) == '<:bnet:424735377106927616>' and '[PC]' not in client.get_guild(payload.guild_id).get_member(payload.user_id).display_name and len(client.get_guild(payload.guild_id).get_member(payload.user_id).display_name) < 28:
                await client.get_guild(payload.guild_id).get_member(payload.user_id).edit(nick=str(client.get_guild(payload.guild_id).get_member(payload.user_id).display_name) + ' [PC]')
                await msg.remove_reaction('xbox:424735397214421004', client.get_guild(payload.guild_id).get_member(payload.user_id))
                await msg.remove_reaction('ps4:424735418219757568', client.get_guild(payload.guild_id).get_member(payload.user_id))
                await msg.remove_reaction('trash:431931243181899777', client.get_guild(payload.guild_id).get_member(payload.user_id))           
            elif str(payload.emoji) == '<:trash:431931243181899777>':
                while True:
                    if '[XB]' in client.get_guild(payload.guild_id).get_member(payload.user_id).display_name:
                        await client.get_guild(payload.guild_id).get_member(payload.user_id).edit(nick=str(client.get_guild(payload.guild_id).get_member(payload.user_id).display_name).replace('[XB]', ''))
                    elif '[XB]' not in client.get_guild(payload.guild_id).get_member(payload.user_id).display_name:
                        break
                while True:
                    if '[PS]' in client.get_guild(payload.guild_id).get_member(payload.user_id).display_name:
                        await client.get_guild(payload.guild_id).get_member(payload.user_id).edit(nick=str(client.get_guild(payload.guild_id).get_member(payload.user_id).display_name).replace('[PS]', ''))
                    elif '[PS]' not in client.get_guild(payload.guild_id).get_member(payload.user_id).display_name:
                        break
                while True:
                    if '[PC]' in client.get_guild(payload.guild_id).get_member(payload.user_id).display_name:
                        await client.get_guild(payload.guild_id).get_member(payload.user_id).edit(nick=str(client.get_guild(payload.guild_id).get_member(payload.user_id).display_name).replace('[PC]', ''))
                    elif '[PC]' not in client.get_guild(payload.guild_id).get_member(payload.user_id).display_name:
                        break
                await msg.remove_reaction('xbox:424735397214421004', client.get_guild(payload.guild_id).get_member(payload.user_id))
                await msg.remove_reaction('ps4:424735418219757568', client.get_guild(payload.guild_id).get_member(payload.user_id))
                await msg.remove_reaction('bnet:424735377106927616', client.get_guild(payload.guild_id).get_member(payload.user_id))
                await msg.remove_reaction('trash:431931243181899777', client.get_guild(payload.guild_id).get_member(payload.user_id))
    except:
        pass        
client.run('')
