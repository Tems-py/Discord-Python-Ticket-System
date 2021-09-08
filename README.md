[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com) 

# Information
Take your time and work your way through the tutorial. If you have any problems, please feel free to contact me via [discord](https://discord.gg/ykF6UfqWgF).

If you are using the ticket system, please give the repository a star and / or create a fork.

# Requirements

- [Python3](https://www.python.org/downloads/) (Tested with version: 3.9.7)
- [Database](https://www.postgresql.org/download/) (I am using a local PostgreSQL-Database)
- [discord.py](https://pypi.org/project/discord.py/) (Tested with version: 1.7.3)
- [asyncpg](https://pypi.org/project/asyncpg/) (Tested with version: 0.24.0)

# How to create a local PostgreSQL Database

1. Download the installer from the [website](https://www.postgresql.org/download/).

2. Start the installation by double-clicking on `postgresql-13.4-1-windows-x64.exe`. 

3. A [setup window](https://cdn.discordapp.com/attachments/885056750519201842/885056792525168640/unknown.png) will pop up. You should see these steps during the installation:

- [Installation Directory](https://cdn.discordapp.com/attachments/885056750519201842/885057796494737429/unknown.png)

- [Select Components](https://cdn.discordapp.com/attachments/885056750519201842/885058027722526770/unknown.png)

- [Data Directory](https://cdn.discordapp.com/attachments/885056750519201842/885058170597285918/unknown.png)

- [Password](https://cdn.discordapp.com/attachments/885056750519201842/885058346447679518/unknown.png) -> **Choose a secure password and don't forget it!**

- [Port](https://cdn.discordapp.com/attachments/885056750519201842/885058792977469480/unknown.png)

- [Advanced Options](https://cdn.discordapp.com/attachments/885056750519201842/885058954097487882/unknown.png)

- [Pre Installation Summary](https://cdn.discordapp.com/attachments/885056750519201842/885059074318798898/unknown.png)

- [Ready to Install](https://cdn.discordapp.com/attachments/885056750519201842/885059197870428170/unknown.png)

4. Start the installation.

5. After the [installation](https://cdn.discordapp.com/attachments/885056750519201842/885060180574875648/unknown.png) is complete, you can click on `Finish`.

6. Open the PostgreSQL folder (`C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PostgreSQL 13`) and double click on [pgAdmin4](https://cdn.discordapp.com/attachments/885056750519201842/885062929664327690/unknown.png).

7. After pgAdmin4 has loaded, it will ask you for the password you chose during the installation.

8. Click on `Servers` on the left side and open `Databases`. You can see that one database with the name `postgres` already exists. 

9. Right click on `Databases` and select `Create Database`. Name it `PostgreSQL-Tickets` and click on save.

10. Open the database and scroll down to `Schemas`. After opening Shemas, you should see `Tables` a little further down.

11. Right click on `Tables` and select `Create Table`. Call it `tickets` and add two columns named `guild_id` and `ticket_id`. [Example](https://cdn.discordapp.com/attachments/885056750519201842/885072018272305212/unknown.png)

12. Fill in your `guild_id` and save the [changes](https://cdn.discordapp.com/attachments/885056750519201842/885082784195051540/unknown.png).

12. Create a second table named `requests` and add four columns: `guild_id`, `channel_name`, `channel_id`, and `user_id`. [Example](https://cdn.discordapp.com/attachments/885056750519201842/885073845541822484/unknown.png)

# Create the same bot for your server
1. Open the [discord developer portal](https://discord.com/developers/applications) and create a new application. 

2. Click on `Bot` on the left side and add a new one. Make sure to enable [Intents](https://cdn.discordapp.com/attachments/885056750519201842/885075848527511622/unknown.png).

3. Open [`data.json`](https://github.com/Sk1pzz/Discord-Ticket-System/blob/main/data.json) and fill in your `bot-token` and `db-password`. (*The one you created at the beginning*)

4. On your discord server: Create a category named `tickets` and a channel also named `tickets`.

5. Start the bot via the command line and type `?ticket` in the tickets channel. You should see this [message](https://cdn.discordapp.com/attachments/885056750519201842/885081261314560020/unknown.png).

6. You can now click on the small envelope below the message. A new channel should appear.

7. That's pretty much all. If you like the system, I would be happy if you put a star on the repository :)

#### If you want to change the embed-message open `ticket.py`.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
```python
@commands.command()
@commands.has_permissions(administrator=True)
async def ticket(self, ctx):

    embed = discord.Embed(
        description="Any questions or concerns? We will be happy to assist you.", 
        color=0x2F3136
    )

    embed.set_author(name="TiLiKas-Tickets")

    embed.add_field(
        name="Have you checked if someone already had the problem?",
        value="To make our work easier, we would be grateful if you first discuss your problem with other members. That takes some work off our shoulders and may also save you some time.",
        inline=False
    )

    embed.set_footer(text="NOTICE : one user can only have three tickets at once!")
    embed.set_thumbnail(url=ctx.me.avatar_url)

    msg = await ctx.send(embed=embed)
    await msg.add_reaction("📩")
```

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

There are three options for the message in the ticket channel.

✅ -> Claim the ticket (*The creator of the ticket cant claim it*)

📌 -> Mention every supporter (*Does not do anything right now - I'm at it!*)

🔒 -> Close the ticket - the channel will be delete after 10 seconds.

After clicking on the lock, the channel will be deleted and a new channel named **ticket-log** will pop up.

# Done

If you did everything correctly your bot should work like in the examples!

Still questions? Join my [discord server](https://discord.gg/ykF6UfqWgF). 

**Please understand that I cannot explain how it works with other databases.**

