import discord
from discord.ext import commands

intents = discord.Intents.all() # or default what did you need, but if you do default, you must add "intents.message_content = True" bc without this bot can not respond

bot = commands.Bot(command_prefix="!", intents=intents) # u can add anyone prefix

@bot.command()
async def filesize(ctx: commands.Context):
  fsl = ctx.filesize_limit # V--- or ctx.reply, but you must then add a another arg (mb str, int etc)
  await ctx.send(f"{round(fsl / 100))}KB") # <--- KB
  await ctx.send(f"{round(fsl / 100024))}MB") # <--- MB

bot.run("YOUR_TOKEN_HERE")
