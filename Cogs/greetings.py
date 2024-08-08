from discord.ext import commands
import discord

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.text_channels, name="powitania")
        if channel:
            await channel.send(f"Witaj na serwerze, {member.mention}!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = discord.utils.get(member.guild.text_channels, name="pożegnania")
        if channel:
            await channel.send(f"{member.name} opuścił serwer.")

def setup(bot):
    bot.add_cog(Greetings(bot))
    
