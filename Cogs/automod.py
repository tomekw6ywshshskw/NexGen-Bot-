from discord.ext import commands

class AutoMod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bad_words = ["przekleństwo1", "przekleństwo2"]

    @commands.Cog.listener()
    async def on_message(self, message):
        if any(word in message.content.lower() for word in self.bad_words):
            await message.delete()
            await message.channel.send(f"{message.author.mention}, nie używaj przekleństw!")
        await self.bot.process_commands(message)

def setup(bot):
    bot.add_cog(AutoMod(bot))
  
