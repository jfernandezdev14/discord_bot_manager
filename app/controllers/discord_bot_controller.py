from discord import Activity, ActivityType, Webhook, RequestsWebhookAdapter, Embed, Color
from discord.ext import commands
from discord import Message

from app.constants import DISCORD_WEBHOOK_URL


class BotController(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        await ctx.send('pong')

    @commands.command(name="webhook")
    async def webhook(self, ctx: commands.Context):
        webhook = Webhook.from_url(
            url=DISCORD_WEBHOOK_URL,
            adapter=RequestsWebhookAdapter()
        )
        embed = Embed(
            title="Nike Flex Advance SE",
            url="https://www.nike.com/t/flex-advance-se-shoe-l7D25p/DB3539-400",
            description="This sneaker is currently discounted",
            colour=Color.red(),
            author="BrickMonitor - Nike Europe",
            footer="https://www.brickmonitor.io",
        )
        embed.set_thumbnail(
            url="https://static.nike.com/a/images/t_default/bc127b4a-e519-4362-ba1e-a7b56da083d4/flex-advance-se-shoe-l7D25p.png")
        embed.add_field(name="Style Code", value="DB3539-400", inline=True)
        embed.add_field(name="Price", value="34", inline=True)
        embed.add_field(name="Brick Score", value="8", inline=True)
        embed.add_field(name="Sizes in stock:", value="8, 8.5, 9, 10.5, 11", inline=False)

        # Finally as your embed message is already defined you can use the function send from webhook class to send your message, is important to define
        # the parameter embed as it is a required param.
        webhook.send(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=Activity(type=ActivityType.watching, name="_help"))
        print('My bot is ready')

    @commands.Cog.listener()
    async def on_message(self, message: Message):
        if message.content == "react":
            i = 0
            for i in range(300):
                emoji = '\N{THUMBS UP SIGN}'
                await message.add_reaction(emoji)
                i = i + 1


def setup(bot: commands.Bot):
    bot.add_cog(BotController(bot))
