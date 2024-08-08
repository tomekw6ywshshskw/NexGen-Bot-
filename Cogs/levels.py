from discord.ext import commands
import discord
import sqlite3
import random

class Levels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            xp = random.randint(5, 15)
            await self.add_xp(message.author.id, xp)
        await self.bot.process_commands(message)

    async def add_xp(self, user_id, xp):
        conn = sqlite3.connect('data/database.db')
        c = conn.cursor()
        c.execute("INSERT OR IGNORE INTO users (user_id, xp) VALUES (?, ?)", (user_id, 0))
        c.execute("UPDATE users SET xp = xp + ? WHERE user_id = ?", (xp, user_id))
        conn.commit()
        conn.close()

def setup(bot):
    bot.add_cog(Levels(bot))
  
