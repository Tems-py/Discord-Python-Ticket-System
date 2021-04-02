import asyncio
import datetime
import discord 
import random

from datetime import datetime
from discord.ext import commands

class Event(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):

        guild_id = payload.guild_id
        guild = self.client.get_guild(guild_id)

        user_id = payload.user_id
        user = self.client.get_user(user_id)

        channel_id = payload.channel_id
        channel = self.client.get_channel(channel_id)

        message_id = payload.message_id
        emoji = payload.emoji.name

        ticket_id = await self.client.db.fetchrow("SELECT ticket_id FROM tickets WHERE guild_id = $1", guild_id)

        if message_id == ticket_id[0] and emoji == "📩":

            message = await channel.fetch_message(message_id)
            await message.remove_reaction("📩",user)

            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            support_role = discord.utils.get(guild.roles, name = "Support")
            category = discord.utils.get(guild.categories, name = "Tickets")

            if support_role is None:

                await guild.create_role(name="Support")

            if category is None:

                    new_category = await guild.create_category(name="Tickets")
                    category = guild.get_channel(new_category.id)

            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                member: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                support_role: discord.PermissionOverwrite(read_messages=True, send_messages=True)
            }

            ticket_channel_name = await category.create_text_channel(f'ticket-{random.randint(100,999)}', overwrites=overwrites)
            ticket_channel_id = ticket_channel_name.id

            await self.client.db.execute("INSERT INTO requests (guild_id, channel_name, channel_id) VALUES ($1, $2, $3)", guild.id, str(ticket_channel_name), ticket_channel_id)

            embed = discord.Embed(title="How can we help you?", description="A supporter will take care of you as soon as \
                 possible.\n\n:white_check_mark: - Claim the ticket\n:no_entry: - Inform the supporters about your ticket\n:lock: - Close the ticket", color=0xf7fcfd)

            embed.set_author(name="TiLiKas Ticket Bot")
            embed.set_image(url="https://cdn.discordapp.com/attachments/762902708319420439/769130943762923590/unknown.png")

            ticket_channel_message = await ticket_channel_name.send(embed=embed)

            await ticket_channel_message.add_reaction("✅")
            await ticket_channel_message.add_reaction("⛔")
            await ticket_channel_message.add_reaction("🔒")

        # ! IMPORT IDs

        db_ticket = await self.client.db.fetch("SELECT channel_id FROM requests WHERE guild_id = $1", guild.id)
        
        db_ticket_channel_id = []
        for db_ticket_id in db_ticket:
            db_ticket_channel_id.append(db_ticket_id["channel_id"])

        if channel_id in db_ticket_channel_id and emoji == "✅" and user.bot == False:

            if user_id:

                embed = discord.Embed(
                    title = "You can't claim the ticket!",
                    color = 0xf7fcfd)
                embed.set_author(name="TiLiKas Ticket Bot")

                await channel.send(embed=embed)

            else:

                embed = discord.Embed(
                    title = "Ticket claimed!",
                    description = f"The ticket was claimed by {user.mention}.",
                    color = 0xf7fcfd)
                embed.set_author(name="TiLiKas Ticket Bot")

                await channel.send(embed=embed)

        if channel_id in db_ticket_channel_id and emoji == "⛔" and user.bot == False:

            embed = discord.Embed(
                title=f"Ticket unprocessed!",
                description="The Supporters are informed about your ticket!",
                color=0xf7fcfd)

            await channel.send(embed=embed)
        
        if channel_id in db_ticket_channel_id and emoji == "🔒" and user.bot == False:

            db_channel_name = await self.client.db.fetchrow("SELECT channel_name FROM requests WHERE channel_id = $1", channel_id)

            embed = discord.Embed(
                title = "Ticket closed!",
                description = f":tickets: The ticket was just closed by {user.mention}.",
                color = 0xf7fcfd)

            await channel.send(embed=embed)
            await asyncio.sleep(10)
            await channel.delete()

            channel_log = discord.utils.get(guild.text_channels, name="ticket-log")
            overwrites = {guild.default_role: discord.PermissionOverwrite(send_messages=False)}

            if channel_log is None:

                channel_log = await guild.create_text_channel("ticket-log", overwrites=overwrites)

            embed = discord.Embed(
                title = "Closed Ticket",
                description = f"The {db_channel_name[0]} was closed by {user.mention}",
                timestamp = datetime.utcnow(),
                color = 0xf7fcfd)

            await channel_log.send(embed=embed)

            await self.client.db.fetch("DELETE FROM requests WHERE channel_id = $1", channel_id)

def setup(client):
    client.add_cog(Event(client))

    
