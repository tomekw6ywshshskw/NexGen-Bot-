from discord.ext import commands
import discord

class ReactionRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        guild = self.bot.get_guild(payload.guild_id)
        role = discord.utils.get(guild.roles, name="TwojaRola")
        if payload.emoji.name == "👍" and role:
            member = guild.get_member(payload.user_id)
            await member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        guild = self.bot.get_guild(payload.guild_id)
        role = discord.utils.get(guild.roles, name="TwojaRola")
        if payload.emoji.name == "👍" and role:
            member = guild.get_member(payload.user_id)
            await member.remove_roles(role)

def setup(bot):
    bot.add_cog(ReactionRoles(bot))
  
