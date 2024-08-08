from discord.ext import commands
import discord

class Verification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def verify(self, ctx):
        role = discord.utils.get(ctx.guild.roles, name="Zweryfikowany")
        if role:
            await ctx.author.add_roles(role)
            await ctx.send(f"{ctx.author.mention}, zostałeś zweryfikowany!")

def setup(bot):
    bot.add_cog(Verification(bot))
  
