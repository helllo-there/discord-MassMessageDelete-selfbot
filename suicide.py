import discord
from discord.ext import commands
import time
import random

bot = commands.Bot(command_prefix="!", self_bot=True, chunk_guilds_at_startup=False)
channel_list = [CHANNEL_ID_1, CHANNEL_ID_2, [GUILD_ID_1, CHANNEL_ID_1]] #etc
# if it's a dm channel, only post the channel id. if it's a server channel, post the guild id and then the channel id in a list (I haven't made a method to use filter this way, either edit the code or just use the prefix method
begin_on_startup = True

async def startup(var): # for parsing through the channel list (if you want to add a guild id or not)
    if len(var) == 2:
        await suicide(var[0], var[1])
        return
    await suicide(var[0])
    return

async def suicide(channel_id, guild_id = None, filter = None): #delete messages in a channel (no guild id if it's a DM channel), and filter by specific content like "hi" idk
    counter, waiting_addon = 0, 0
    if not guild_id:
        try:
            channel = await bot.fetch_channel(channel_id)
        except:
            print(f"Invalid channel ID: {channel_id}")
            return
        print(f"Total messages in channel: {len([msg async for msg in channel.history(limit=None)])}")
    else:
        try:
            guild = bot.get_guild(guild_id)
            channel = guild.get_channel(channel_id)
        except:
            print(f"Invalid channel ID {channel_id} or guild ID {guild_id}")
            return
        print("Not showing total messages - not a DM channel")
    
    async for message in channel.history(limit=None):
        if message.author == bot.user and (not filter or filter in message.content):
            await message.delete()
            counter += 1
            print(counter, message.content)
            time.sleep(random.uniform(1.2165 + waiting_addon, 1.5878 + waiting_addon)) # random sleep time between each message, simulate a real person ig
        elif not guild_id: # if we're in a DM channel, we wait between each message to kinda simulate a real person deleting messages. if on a server, don't bother cuz its too long
            time.sleep(random.uniform(0.1949, 0.7001))
    print(f"{counter} messages deleted.")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('Selfbot is ready!')
    if begin_on_startup:
        for channel in channel_list:
            startup(channel)

# or, we do it when the user sends a message in whatever channel
@bot.event
async def on_message(message):
    if message.author == bot.user and message.content.startswith("$ suicide"):
        suicide(message.channel.id, message.channel.guild.id, message.content.split()[1] if len(message.content.split()) > 1 else None)

bot.run('TOKEN')

# known issues: Won't delete messages from a user app in a dm channel
