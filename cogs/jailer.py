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

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        """on_ready executes once the bot has connected to Discord"""
        print(f"{self.bot.user.name} has connected to Discord!")

    @commands.command(
        brief="Jails a users",
        description="This Commands Jails the user mentioned"
    )
    @commands.has_role("Admin")
    @commands.has_role("OP")
    async def jail(self, ctx, member: discord.Member):
        op_role = discord.utils.get(ctx.guild.roles, name="OP")
        boomer_role = discord.utils.get(ctx.guild.roles, name="Boomer")
        jailed_role = discord.utils.get(ctx.guild.roles, name="Jailed")
        if op_role in member.roles or boomer_role in member.roles:
            await ctx.send(
                "Can't jail "
                f"{member}")
            return
        if jailed_role in member.roles:
            return
        await member.edit(roles=[])
        await member.add_roles(jailed_role)
        jail_channel = discord.utils.get(ctx.guild.channels, name="horny-jail")
        await jail_channel.send(
            "{} You have been jailed for rule violation".format(member.mention)
        )

    @commands.command(
        brief="Removes users from jail",
        description="This Commands removes the user mentioned from jail"
    )
    @commands.has_role("Admin")
    @commands.has_role("OP")
    async def release(self, ctx, member: discord.Member):
        op_role = discord.utils.get(ctx.guild.roles, name="OP")
        boomer_role = discord.utils.get(ctx.guild.roles, name="Boomer")
        member_role = discord.utils.get(ctx.guild.roles, name="Member")
        jailed_role = discord.utils.get(ctx.guild.roles, name="Jailed")
        if op_role in member.roles and boomer_role in member.roles:
            return
        if jailed_role not in member.roles:
            return
        await member.remove_roles(jailed_role)
        await member.add_roles(member_role)
        jail_channel = discord.utils.get(ctx.guild.channels, name="horny-jail")
        await jail_channel.send(
            f"{member}"
            f" has been freed from jail"
        )


def setup(bot):
    bot.add_cog(Jailer(bot))
