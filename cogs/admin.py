import discord
import asyncio
from discord.ext import commands


class AdminCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ticket(self, ctx):
        title = "Would you like to create a ticket?"
        description = "If you have a question or concern, please create a ticket by clicking on the 📩 emoji."
        name = "If you have any general questions about the ticket system please contact a supporter!" 

        embed = discord.Embed(title=title, description=description, color=0x2f2fd0)
        embed.add_field(name="General questions!", value=name, inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/771635939700768769/773121323341578250/external-content.duckduckgo.com.png")
        embed.set_author(name="TiLiKas Support Bot")

        msg = await ctx.send(embed=embed)
        await msg.add_reaction("📩")
        await ctx.message.delete()
        
def setup(client):
    client.add_cog(AdminCommands(client))
