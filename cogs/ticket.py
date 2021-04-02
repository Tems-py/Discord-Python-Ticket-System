import discord 

from discord.ext import commands

class Ticket(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ticket(self, ctx):

        embed = discord.Embed(
            title="Would you like to create a ticket?", 
            description="If you have any questions or concerns create a new ticket by clicking on the emoji below this message.", 
            color=0xf7fcfd)

        embed.add_field(name="Do you want to report someone?", value="Please contact a supporter or moderator directly!", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/771635939700768769/773121323341578250/external-content.duckduckgo.com.png")
        embed.set_author(name="TiLiKas-Tickets")

        msg = await ctx.send(embed=embed)
        await msg.add_reaction("📩")

def setup(client):
    client.add_cog(Ticket(client))