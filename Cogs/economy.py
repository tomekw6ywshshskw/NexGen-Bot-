from discord.ext import commands
import sqlite3

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def balance(self, ctx):
        balance = await self.get_balance(ctx.author.id)
        await ctx.send(f"{ctx.author.mention}, twój stan konta wynosi: {balance} punktów.")

    @commands.command()
    async def give(self, ctx, member: discord.Member, amount: int):
        await self.add_balance(ctx.author.id, -amount)
        await self.add_balance(member.id, amount)
        await ctx.send(f"Przekazałeś {amount} punktów użytkownikowi {member.mention}.")

    async def get_balance(self, user_id):
        conn = sqlite3.connect('data/database.db')
        c = conn.cursor()
        c.execute("SELECT balance FROM users WHERE user_id = ?", (user_id,))
        balance = c.fetchone()
        conn.close()
        return balance[0] if balance else 0

    async def add_balance(self, user_id, amount):
        conn = sqlite3.connect('data/database.db')
        c = conn.cursor()
        c.execute("INSERT OR IGNORE INTO users (user_id, balance) VALUES (?, ?)", (user_id, 0))
        c.execute("UPDATE users SET balance = balance + ? WHERE user_id = ?", (amount, user_id))
        conn.commit()
        conn.close()

def setup(bot):
    bot.add_cog(Economy(bot))
  
