import discord
from discord.ext import commands

# Create a new Discord bot instance
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.command()
async def feedback(ctx, *, message):
    # Send the feedback to a designated channel or process it
    print(f'Feedback received: {message}')
    await ctx.send('Thank you for your feedback!')

# Run the bot with your token
bot.run('YOUR_DISCORD_TOKEN')