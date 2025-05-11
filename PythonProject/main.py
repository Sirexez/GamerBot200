import asyncio
import tracemalloc

import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import Tables
import requests
import robloxpy
import random
import time
tracemalloc.start()

load_dotenv()
token = os.getenv('DISCORD_TOKEN')



async def send_dm(ctx, member:discord.Member, *, content):
  await member.send(content)

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents, case_insensitive=True)
sirexez = ""
guild = ""
channel = ""
currentprogress = 25

@bot.event
async def on_ready():
    global guild
    guild = bot.get_guild(1141889049041326080)
    global channel
    channel = bot.get_channel(1141889049569804431)
    global sirexez
    sirexez = guild.get_member(633455643675590656)

@bot.event
async def on_member_join(member):
    await member.send(f"Oh yessss I cant stop goooooning yeeessss")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    # await message.channel.send(message.author)
    if "gamerman" in message.content.lower():
        await message.channel.send(f"{message.author.mention} - Gamerman Is Top 1 NA!!!")

    await bot.process_commands(message)

@bot.event
async def on_message_delete(message):
    if message.author == bot.user:
        return
    await sirexez.send(f"{message.author} deleted his fuckin message that said: {message.content}")

class RankDropdown(discord.ui.Select):
    def __init__(self):
        options = [discord.SelectOption(label="S"), discord.SelectOption(label="Levi")]

        super().__init__(placeholder="Tier", options=options, min_values=1, max_values=1)
    async def callback(self, interaction: discord.Interaction):
        Table = Tables.AbaTierTables[str(self.values[0])]
        message = random.randint(0, len(Table))
        await interaction.response.send_message(f"You got : **`{Table[message]}`** {interaction.user.mention}")
        await interaction.message.delete()

class RankDropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(RankDropdown())

GUILD_ID = discord.Object(id=1141889049041326080)

@bot.tree.command(name="commandlist", guild=GUILD_ID, description="List of commands used by the GamerBot")
async def cmds(ctx):
    await ctx.response.send_message(Tables.CommandList)

@bot.command()
async def cmds(ctx):
    await ctx.send(Tables.CommandList)

@bot.command()
async def progress(ctx):
    await ctx.send(f"{currentprogress} Percent DONE! (it's never coming out)\nNext test on 6/15")

@bot.command()
async def Is_Luca_Trash(ctx):
    await ctx.send(f"Yeah lucas fuckin ass bro")

@bot.command()
async def cheese(ctx):
    await ctx.send(f"Brooo {ctx.author} ur such a cheeser")

@bot.command()
async def randomgif(ctx):
     message = random.randint(0, Tables.AmountOfGifs)
     await ctx.send(Tables.Gifs[message])

@bot.command()
async def gif(ctx):
     message = random.randint(0, Tables.AmountOfGifs)
     await ctx.send(Tables.Gifs[message])

@bot.command()
async def wisequote(ctx):
     message = random.randint(0, Tables.AmountOfWiseQuotes)
     await ctx.send(Tables.WiseQuotes[message])

@bot.command()
async def randomabacharacter(ctx):
     await ctx.send("Which tier of characters do you want to pick from?", view=RankDropdownView())

@bot.command()
async def gn(ctx):
    await ctx.send(f"Goodnight krooooski")

async def randommessageloop():
    while True:
        message = random.randint(1, Tables.AmountOfGifs)
        channel = bot.get_channel(1141889049569804431)
        await channel.send(Tables.Gifs[message])
        time.sleep(900)

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
