import discord
import os
from discord.ext import commands

intents = discord.Intents.all() # You can also add "discord.Intents.default()" and then "message_content = True", but I use "discord. Intents.all()".

bot = commands.Bot(command_prefix="!", intents=intents) # You can give any prefix you want

@bot.command()
async def filesize(ctx: commands.Context):
  file_limit = ctx.filesize_limit
  await ctx.send(f"{round(file_limit / 100))}KB") # <--- Kilobytes
  await ctx.send(f"{round(file_limit / 100024))}MB") # <--- Megabytes

token = os.environ["fsl_token"]

bot.run(token)
