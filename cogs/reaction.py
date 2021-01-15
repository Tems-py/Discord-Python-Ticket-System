import discord
import random
import asyncio
import datetime

from discord.ext import commands
from discord.utils import get
from time import strftime
from datetime import datetime

class Reaction(commands.Cog):

    def __init__(self, client):
        self.client = client

    channel_ticket = None
    ticket_creator = None

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        guild_id = payload.guild_id
        guild = self.client.get_guild(guild_id)
        user_id = payload.user_id
        user = self.client.get_user(user_id)
        message_id = payload.message_id
        channel = self.client.get_channel(payload.channel_id)

        # TICKETS
        emoji = payload.emoji.name
        
        if message_id == MESSAGE_ID and emoji == "📩":

            self.ticket_creator = user_id

            message = await channel.fetch_message(message_id)
            await message.remove_reaction("📩",user)

            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            support_role = guild.get_role(ROLE_ID)
            category = guild.get_channel(CATEGORY_ID)
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                member: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                support_role: discord.PermissionOverwrite(read_messages=True, send_messages=True)
            }
            ticket_nr = random.randint(100,999)
            self.channel_ticket = await category.create_text_channel(f'ticket-{ticket_nr}', overwrites=overwrites)

            embed = discord.Embed(
                title="How can we help you?",
                description="A supporter will take care of you as soon as possible.\n\n:white_check_mark: - Claim the ticket\n:no_entry: - Inform the supporters about your ticket\n:lock: - Close the ticket", 
                color=0x0000ff)
            embed.set_author(name="TiLiKas Ticket Bot")
            embed.set_image(url="https://cdn.discordapp.com/attachments/762902708319420439/769130943762923590/unknown.png")

            msg = await self.channel_ticket.send(embed=embed)

            await msg.add_reaction("✅")
            await msg.add_reaction("⛔")
            await msg.add_reaction("🔒")
        
        if channel == self.channel_ticket and emoji == "⛔" and user_id != BOT_ID:
            
            message = await channel.fetch_message(message_id)
            await message.remove_reaction("⛔",user)

            await channel.send(f"The ticket ``{self.channel_ticket}`` is now unprocessed for more than 10 minutes! <@&ROLE_ID>")

        if channel == self.channel_ticket and emoji == "🔒" and user_id != BOT_ID:
            
            message = await channel.fetch_message(message_id)
            await message.remove_reaction("🔒",user)

            now = datetime.now()   
            time = now.strftime(str("%d.%m.%Y") + " at " + str("%H:%M"))

            channel_log = self.client.get_channel(LOG_CHANNEL_ID)
            text = f"The ticket ``{self.channel_ticket}`` was closed by {user.mention} on {time}"

            embed = discord.Embed(
                title = "Closed Ticket",
                description = text,
                color = 0x0000ff)

            await channel_log.send(embed=embed)

            embed = discord.Embed(
                title = "Ticket closed!",
                description = f":tickets: The ticket was just closed by {user.mention}.",
                color = 0x0000ff)

            await channel.send(embed=embed)

            await asyncio.sleep(10)

            await channel.delete()

        if channel == self.channel_ticket and emoji == "✅" and user_id != BOT_ID:

            message = await channel.fetch_message(message_id)
            await message.remove_reaction("✅",user)

            if self.ticket_creator == user_id:

                embed = discord.Embed(
                    title = "You cant claim the ticket!",
                    color = 0x0000ff)
                embed.set_author(name="TiLiKas Ticket Bot")

                await channel.send(embed=embed)

            else:

                embed = discord.Embed(
                    title = "Ticket claimed!",
                    description = f"The ticket was claimed by {user.mention}.",
                    color = 0x0000ff)
                embed.set_author(name="TiLiKas Ticket Bot")

                await channel.send(embed=embed)

def setup(client):
    client.add_cog(Reaction(client))
