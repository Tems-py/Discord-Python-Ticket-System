# Ticket-Bot
A discord ticket system with PostgreSQL.

# Information
This is not supposed to be a copy and paste exercise, if you want to recreate the system, learn python first. 

If you have any improvement suggestions feel free to contact me.

### NOT for beginners of discord.py!

If you are completly new to discord.py or generally python - DO NOT JUST copy the code - study the syntax first and try slightly easier projects. 

# Requirements

- Python 3.8.6 or higher
- discord.py (Tested with version 1.6.0)
- PostgreSQL Database (I am using a local PostgreSQL Database)
- asyncpg

# How to create a local PostgreSQL Database

1. Download the installer from the [website](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads).

2. After the download is complete start the installation by double-clicking on the .exe. 

3. A Setup-Window should show up. Just keep clicking on NEXT until the [password window](https://cdn.discordapp.com/attachments/771635939700768769/827816815886991380/unknown.png). 

4. **Choose a good and secure password and remember it!** 

5. You can use the default settings for the next two windows.

6. Now start the [installation](https://cdn.discordapp.com/attachments/771635939700768769/827819917829996554/unknown.png).

7. After the installation is finished you shuold see this [windows](https://cdn.discordapp.com/attachments/771635939700768769/827813661182525460/unknown.png). You dont need to launch Stack-Builder - just click on finish. 

8. Now click on Windows and search for PostgreSQL. Open the folder and click on [pgAdmin4](https://cdn.discordapp.com/attachments/771635939700768769/827823887495856128/unknown.png).

9. After it loads, it asks for the [password](https://cdn.discordapp.com/attachments/771635939700768769/827824348562849802/unknown.png) you used during the installation.

10. Click on **Servers** on the left side and open **Databases**. You can see that one with the name **postgres** already exists. 

11. Right-Click on Databases and select **Create Database**. Take **PostgreSQL-Tickets** as the name and click on save.

12. The Database should appear on the left side. Open it and scroll down to **Schemas**. If you have Schemas open, you will find **Tables** below. 

13. Right-Click on Tables and create a new one. Call it **tickets**. Add two columns named ``guild_id (PK)`` and ``ticket_id``. It should look like [this](https://cdn.discordapp.com/attachments/771635939700768769/827830274615935026/Unbenannt.png).

14. Add another Table named **requests** with three columns named ``guild_id``, ``channel_name`` and ``channel_id``. Like [this](https://cdn.discordapp.com/attachments/771635939700768769/827829056945782784/unknown.png).

15. Now the database setup is finished -  dont close it now you will need it later again.

# How to create the same bot for your server
1. Go on the [discord developer portal](https://discord.com/developers/applications) and make a new application. Now create a new bot and add him to your server.

2. Create a database named ``PostgreSQL-Tickets`` and add two tables. ([tutorial](https://www.youtube.com/watch?v=hSPhZTCAvG0)) 

3. Name the first table ``tickets`` and the second one ``requests``. 

4. Add two columns (guild_id and ticket_id) to the [tickets-table](https://cdn.discordapp.com/attachments/771635939700768769/827459057223860254/unknown.png). (*Make sure that ``guild_id`` is a primary key.*)

5. Add three columns (guild_id, channel_name and channel_id) to the [requests-table](https://cdn.discordapp.com/attachments/771635939700768769/827459186870190100/unknown.png). (*No primary key needed!*)

6. Start the bot and type ``?ticket`` in your ticket-channel. A message like [this](https://cdn.discordapp.com/attachments/771635939700768769/827460503185653790/unknown.png) should pop up.

7. Now copy the ID of your server and the message you just created and fill it in the database. Your DB should look like [this](https://cdn.discordapp.com/attachments/771635939700768769/827460984628183060/unknown.png).

8. If you are done, restart the bot and click on the 📩. You should see a new channel with a [message](https://cdn.discordapp.com/attachments/771635939700768769/827462375803191326/unknown.png) inside.

#### If you want to change the embed-message open ``ticket.py``.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
```python
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
```
**I would recommend to change the authors-name (TiLiKas-Tickets)**

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Now you have three diffrent emoji choices:

✅ -> Claim the ticket (*The creator of the ticket cant claim it*)

⛔ -> Mention every supporter (*Does not do anything right now - I'm at it!*)

🔒 -> Close the ticket - the channel will be delete after 10 seconds.

# Done

If you did everything correctly your bot should work like in the examples!

Still questions? Join my [discord server](https://discord.gg/ykF6UfqWgF).

I will not reply to basic questions like "How can I start my bot" or if the error message clearly states what is not working. 

As I wrote at the beginning, this tutorial is not for complete beginners.

