# Ticket-Bot
This is a public repository for my discord ticket system

# Information
Please notice that this is just an pretty basic example of a ticket-bot.
I will constantly try to improve and upgrade the bot.

If you have any suggestions for improvements feel free to contact me 

### For beginners of discord.py!

If you are completly new to discord.py or generally python - I would not recommend to just copy the code - study the discord.py syntax first and try a slightly easier project. 
While it may seems straightforward to advanced users, it can be confusing for newbies.

# Requirements

- Python 3.8.6 ([download](https://www.python.org/downloads/release/python-386/))
- discord.py (pip install -U discord.py[voice]) (Tested with version 1.6.0)

# How to create the same bot for your server
1. Go on the [discord developer portal](https://discord.com/developers/applications) and create a bot.

2. Add the bot to your server.

3. Create a directory where you want your code to be - If you donwloaded the ZIP just extract the foler and paste it into the new created directory! - remember the path - you need to start the bot from it

4. After you downloaded everything go to ``token.txt`` and change ``PASTE_YOUR_TOKEN_IN_HERE`` with the token from your [bot](https://discord.com/developers).

5. Next open the ``cogs`` folder - in the folder are two files ``admin.py`` and ``reaction.py``.

6. Open ``admin.py`` - your code should look like this:

---------------------------------------------------------------------------------------------------------------------------------------------------------------------
```python
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
```
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can change the text of the embed however you want - **change the name of the author in the embed (TiLiKas Support Bot)**

6. Go on your discord server and create a category called ``tickets``.

7. Create two channels. One called ``tickets`` and the other one ``log-channel``.

7. Start the bot and type ``?ticket`` in the ``tickets`` channel.

If you did everything correctly you will see a message like [this](https://cdn.discordapp.com/attachments/771635939700768769/798486004981039107/unknown.png).

8. After you are done navigate to the folder where your bot is saved and open ``reaction.py``.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------
```python
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
```
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Now you need to make a few changes:

-> Change ``MESSAGE_ID`` to the ID of the [message](https://cdn.discordapp.com/attachments/771635939700768769/798486563449208842/unknown.png).

-> Change ``ROLE_ID`` to the ID of the role that should have access to the tickets (f.e. [Support](https://media.discordapp.net/attachments/771635939700768769/798486693945540628/unknown.png)) (*There is also a ROLE_ID on line 67*)

-> Change ``CATEGORY_ID`` to the ID of the [category](https://cdn.discordapp.com/attachments/771635939700768769/798486814217863228/unknown.png) you created

-> Change ``BOT_ID`` to the ID of your bot

-> Change ``LOG_CHANNEL_ID`` to the ID of the channel where you want to get the information if a ticket gets closed

**ALSO dont forget to change the authors name to the name of your bot!**

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

9. Restart the bot and klick on 📩  - it should look like [this](https://cdn.discordapp.com/attachments/771635939700768769/798487685471797328/unknown.png)

You have three diffrent emoji choices:

✅ -> Claim the ticket ([example](https://cdn.discordapp.com/attachments/771635939700768769/798489702093029376/unknown.png)) (*The creator of the ticket cant claim it*)

⛔ -> Mention every supporter ([example](https://cdn.discordapp.com/attachments/771635939700768769/798487939063087133/unknown.png))

🔒 -> Close the ticket - channel will delete itself after 10 seconds ([example](https://cdn.discordapp.com/attachments/771635939700768769/798488068038328330/unknown.png))

**After closing the ticket it will no longer be accessable**

# LOG - Channel

If you dont want to use this channel just delete this part:

```python
now = datetime.now()   
time = now.strftime(str("%d.%m.%Y") + " at " + str("%H:%M"))

channel_log = self.client.get_channel(LOG_CHANNEL_ID)
text = f"The ticket ``{self.channel_ticket}`` was closed by {user.mention} on {time}"

embed = discord.Embed(
    title = "Closed Ticket",
    description = text,
    color = 0x0000ff)

await channel_log.send(embed=embed)
```

**You can also remove these imports:**

- import datetime
- from time import strftime
- from datetime import datetime

# Done

If you did everything correctly the bot should work like in the examples!

Still questions? Join my [discord server](https://discord.gg/WRH22qat76)

(I will not reply to E-Mails)
