from discord.ext import commands
import sqlite3
import random

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def balance(self, ctx):
        balance = await self.get_balance(ctx.author.id)
        await ctx.send(f"{ctx.author.mention}, twój stan konta wynosi: {balance} punktów.")

    @commands.command()
    async def give(self, ctx, member: discord.Member, amount: int):
        if amount <= 0:
            await ctx.send("Kwota musi być większa niż zero.")
            return
        await self.add_balance(ctx.author.id, -amount)
        await self.add_balance(member.id, amount)
        await ctx.send(f"Przekazałeś {amount} punktów użytkownikowi {member.mention}.")

    @commands.command()
    async def work(self, ctx):
        earnings = random.randint(50, 150)
        await self.add_balance(ctx.author.id, earnings)
        await ctx.send(f"{ctx.author.mention}, zarobiłeś {earnings} punktów!")

    @commands.command()
    async def gamble(self, ctx, amount: int):
        balance = await self.get_balance(ctx.author.id)
        if amount > balance:
            await ctx.send("Nie masz wystarczająco dużo punktów.")
            return
        if amount <= 0:
            await ctx.send("Kwota musi być większa niż zero.")
            return

        if random.randint(1, 2) == 1:
            winnings = amount * 2
            await self.add_balance(ctx.author.id, winnings)
            await ctx.send(f"Gratulacje! Wygrałeś {winnings} punktów.")
        else:
            await self.add_balance(ctx.author.id, -amount)
            await ctx.send(f"Niestety przegrałeś {amount} punktów.")

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
                                   
