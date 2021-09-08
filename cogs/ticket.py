import discord 

from discord.ext import commands

class Ticket(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ticket(self, ctx):

        embed = discord.Embed(
            description="Any questions or concerns? We will be happy to assist you.", 
            color=self.client.color
        )

        embed.set_author(name="TiLiKas-Tickets")

        embed.add_field(
            name="Have you checked if someone already had the problem?",
            value="To make our work easier, we would be grateful if you first discuss your problem with other members. That takes some work off our shoulders and may also save you some time.",
            inline=False
        )

        embed.set_footer(text="NOTICE : one user can only have three tickets at once!")
        embed.set_thumbnail(url="https://i.imgur.com/OG3IJF9.png")

        msg = await ctx.send(embed=embed)
        await msg.add_reaction("📩")

        await self.client.db.execute("UPDATE tickets SET ticket_id = $2 WHERE guild_id = $1", ctx.guild.id, msg.id)

        embed = discord.Embed(color=self.client.color)
        embed.set_author(name="Successfully created the ticket-system.")

        confirmEmbed = await ctx.send(embed=embed)
        await confirmEmbed.delete(delay=10)

def setup(client):
    client.add_cog(Ticket(client))
