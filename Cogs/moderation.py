from discord.ext import commands
import discord

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} został zbanowany. Powód: {reason}")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} został wyrzucony. Powód: {reason}")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def warn(self, ctx, member: discord.Member, *, reason=None):
        # W praktyce możesz dodać logikę do zapisywania ostrzeżeń do bazy danych
        await ctx.send(f"{member.mention} otrzymał ostrzeżenie. Powód: {reason}")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member, duration: int, *, reason=None):
        mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not mute_role:
            mute_role = await ctx.guild.create_role(name="Muted")
            for channel in ctx.guild.channels:
                await channel.set_permissions(mute_role, speak=False, send_messages=False)
        
        await member.add_roles(mute_role, reason=reason)
        await ctx.send(f"{member.mention} został wyciszony na {duration} minut. Powód: {reason}")
        
        # Logika odwołująca mute po czasie
        await asyncio.sleep(duration * 60)
        await member.remove_roles(mute_role)
        await ctx.send(f"{member.mention} został odciszony.")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: discord.Member):
        mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(mute_role)
        await ctx.send(f"{member.mention} został odciszony.")

def setup(bot):
    bot.add_cog(Moderation(bot))
  
