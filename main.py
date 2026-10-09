import discord
from discord.ext import commands
import random

token = "YOUR_BOT_TOKEN_HERE"  # Replace with yours

bot = commands.Bot(
    command_prefix=">",
    intents=discord.Intents.all(),
    strip_after_prefix=True
)

RESPONSES = [
    "Yes, absolutely.",
    "No way.",
    "Outlook hazy, try again.",
    "Signs point to yes.",
    "Don't count on it.",
    "Ask again after coffee.",
]

@bot.event
async def on_ready():
    print("Bot is ready!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if bot.user.mentioned_in(message):
        await message.channel.send("Hello! Use `>ask <your question>` to ask me anything.")
    
    if message.content.startswith(">random"):
        await message.channel.send(random.randint(1, 100))

    await bot.process_commands(message)

@bot.command(name="ask")
async def ask(ctx: commands.Context, *, question: str):
    answer = random.choice(RESPONSES)
    await ctx.reply(f"{answer}")

@ask.error
async def ask_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply(
            "You forgot to provide a question!"
        )

bot.run(token)