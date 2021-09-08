import asyncio
import datetime
import random
import discord

from datetime import date, datetime
from discord import guild
from discord.ext import commands
from discord.utils import get


class Events(commands.Cog):

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

        ######################### TICKETS #########################

        if emoji == "📩" and not user.bot:

            query = """SELECT ticket_id FROM tickets WHERE guild_id = $1"""
            ticket_id = await self.client.db.fetchrow(query, guild_id)

            if message_id == ticket_id[0]:

                message = await channel.fetch_message(message_id)
                await message.remove_reaction("📩", user)

                query = """SELECT COUNT(user_id) FROM requests WHERE guild_id = $1 AND user_id = $2"""
                ticket_count = await self.client.db.fetch(query, guild_id, user_id)

                if ticket_count[0]["count"] > 2:

                    try:

                        embed = discord.Embed(color=0x2F3136)
                        embed.title = "You already have three pending tickets!"
                        embed.description = "Please close your open tickets before creating new ones."
                        return await user.send(embed=embed)

                    except Exception:
                        return

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

                query = """INSERT INTO requests (guild_id, channel_name, channel_id, user_id) VALUES ($1, $2, $3, $4)"""
                await self.client.db.execute(query, guild.id, str(ticket_channel_name), ticket_channel_name.id, user_id)

                embed = discord.Embed(title="How can we help you?", color=0x2F3136)
                embed.add_field(name="✅ Claim the Ticket!", value="```Claim the ticket so that the other supporters know that it is already being processed.```", inline=False)
                embed.add_field(name="📌 Inform the Support about your Ticket", value="```Inform the other supporters about your ticket to guarantee a quick processing.```", inline=False)
                embed.add_field(name="🔒 Close the Ticket!", value="```Close the ticket as soon as the problem has been resolved.```", inline=False)

                embed.set_author(name="TiLiKas Ticket Bot")
                embed.set_image(url="https://i.imgur.com/BLUcmmJ.png")

                ticket_channel_message = await ticket_channel_name.send(embed=embed)

                await ticket_channel_message.add_reaction("✅")
                await ticket_channel_message.add_reaction("📌")
                await ticket_channel_message.add_reaction("🔒")

        if emoji == "✅" and user.bot == False:

            query = """SELECT channel_id FROM requests WHERE guild_id = $1"""
            ticket_ids = await self.client.db.fetch(query, guild.id)
            ticket_channel_ids = []

            for ticket_id in ticket_ids:
                ticket_channel_ids.append(ticket_id["channel_id"])

            if channel_id in ticket_channel_ids:
                
                query = """SELECT user_id FROM requests WHERE channel_id = $1"""
                db_user = await self.client.db.fetch(query, channel_id)
                db_ticket_channel_users = []

                for ticket_user in db_user:
                    db_ticket_channel_users.append(ticket_user["user_id"])

                if user_id in db_ticket_channel_users:

                    embed = discord.Embed(
                        description="**You can't claim the ticket!**",
                        color=0x2F3136
                    )

                    await channel.send(embed=embed)

                else:

                    embed = discord.Embed(
                        description = f"**The ticket was claimed by {user.name}.**",
                        color = 0x2F3136)

                    await channel.send(embed=embed)
        
        if emoji == "🔒" and user.bot == False:

            query = """SELECT channel_id FROM requests WHERE guild_id = $1"""
            ticket_ids = await self.client.db.fetch(query, guild.id)
            ticket_channel_ids = []

            for ticket_id in ticket_ids:
                ticket_channel_ids.append(ticket_id["channel_id"])

            if channel_id in ticket_channel_ids:

                query = """SELECT channel_name FROM requests WHERE channel_id = $1"""
                db_channel_name = await self.client.db.fetchrow(query, channel_id)

                embed = discord.Embed(
                    description = f"**The ticket was closed by {user.name}.**",
                    color = 0x2F3136)

                await channel.send(embed=embed)
                await asyncio.sleep(10)
                await channel.delete()

                channel_log = discord.utils.get(guild.text_channels, name="overall-log")
                overwrites = {guild.default_role: discord.PermissionOverwrite(send_messages=False)}

                if channel_log is None:
                    channel_log = await guild.create_text_channel("overall-log", overwrites=overwrites)

                embed = discord.Embed(
                    description = f"The **{db_channel_name[0]}** was closed by **{user.name}**",
                    timestamp = datetime.utcnow(),
                    color = 0x2F3136)

                await channel_log.send(embed=embed)
                await self.client.db.fetch("DELETE FROM requests WHERE channel_id = $1", channel_id)


def setup(client):
    client.add_cog(Events(client))
