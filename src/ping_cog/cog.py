import os
from logging import getLogger

from discord.ext import commands
from discord_slash import cog_ext, SlashContext

guild_ids = os.environ.get('guild_ids')
if guild_ids is not None:
    guild_ids = list(map(lambda x: int(x), guild_ids.split(',')))

logger = getLogger(__name__)


class PingCog(commands.Cog):
    """スラッシュコマンドのサンプルのCog"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener('on_ready')
    async def on_ready(self):
        logger.debug('PingCog is ready')

    @cog_ext.cog_slash(name='ping', description='ping pong', guild_ids=guild_ids)
    async def ping(self, ctx: SlashContext):
        logger.debug(f'/ping')
        await ctx.send('pong')


def setup(bot):
    return bot.add_cog(PingCog(bot))
