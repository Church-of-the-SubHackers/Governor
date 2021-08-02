import discord
from discord.ext import commands


class Jailer(commands.Cog):
    """
    Implements Jailer functions
    """

    def __init__(self, bot):
        """
        cog initialization
        Args:
            bot (discord.ext.commands.Bot): Instance of the bot
        """
        self.bot = bot

    @commands.command(
        brief="Jails a users",
        description="This Commands Jails the user mentioned"
    )
    @commands.has_any_role("Admin", "OP")
    async def jail(self, ctx, member: discord.Member):
        op_role = discord.utils.get(ctx.guild.roles, name="OP")
        boomer_role = discord.utils.get(ctx.guild.roles, name="Boomers")
        jailed_role = discord.utils.get(ctx.guild.roles, name="Jailed")
        if op_role in member.roles or boomer_role in member.roles:
            await ctx.send(
                "Can't jail "
                f"{member}")
            return
        if jailed_role in member.roles:
            return
        await member.edit(roles=[jailed_role])
        jail_channel = discord.utils.get(ctx.guild.channels, name="horny-jail")
        await jail_channel.send(
            "{} You have been jailed for rule violation".format(member.mention)
        )

    @commands.command(
        brief="Removes users from jail",
        description="This Commands removes the user mentioned from jail"
    )
    @commands.has_any_role("Admin", "OP")
    async def release(self, ctx, member: discord.Member):
        op_role = discord.utils.get(ctx.guild.roles, name="OP")
        boomer_role = discord.utils.get(ctx.guild.roles, name="Boomers")
        member_role = discord.utils.get(ctx.guild.roles, name="Member")
        jailed_role = discord.utils.get(ctx.guild.roles, name="Jailed")
        if op_role in member.roles or boomer_role in member.roles:
            return
        if jailed_role not in member.roles:
            return
        await member.edit(roles=[member_role])
        jail_channel = discord.utils.get(ctx.guild.channels, name="horny-jail")
        await jail_channel.send(
            f"{member}"
            f" has been freed from jail"
        )


def setup(bot):
    bot.add_cog(Jailer(bot))
