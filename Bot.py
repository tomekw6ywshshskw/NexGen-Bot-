import discord
from discord.ext import commands
import sqlite3
from web.app import create_app

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Załaduj wszystkie cogi
initial_extensions = [
    'cogs.greetings',
    'cogs.autorole',
    'cogs.reaction_roles',
    'cogs.levels',
    'cogs.economy',
    'cogs.automod',
    'cogs.verification'
]

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

# Uruchomienie Flask jako osobnego procesu
app = create_app()

if __name__ == '__main__':
    bot.loop.create_task(app.run(host='0.0.0.0', port=5000))
    bot.run('TWOJ_TOKEN')
    
