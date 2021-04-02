# Ticket-Bot
A discord ticket system with PostgresQL

# Information
This is not supposed to be a copy and paste exercise, if you want to recreate the system, learn the python basics first. 

If you have any improvement suggestions feel free to contact me.

### For beginners of discord.py!

If you are completly new to discord.py or generally python - DO NOT JUST copy the code - study the syntax first and try slightly easier projects. 

# Requirements

- Python 3.8.6 ([download](https://www.python.org/downloads/release/python-386/))
- discord.py (pip install -U discord.py[voice]) (Tested with version 1.6.0)
- PostgresSQL Database (https://www.postgresql.org/download/) (or anything similar)
- pip install asyncpg

# How to create the same bot for your server
1. Go on the [discord developer portal](https://discord.com/developers/applications) and make a new application. Now create a new bot and add him to your server.

2. Create a database named ``PostgresSQL-Tickets`` and add two tables.  

3. Name the first table ``tickets`` and the second one ``requests``. 

4. Add two columns (guild_id and ticket_id) to the [tickets-table](https://cdn.discordapp.com/attachments/771635939700768769/827459057223860254/unknown.png). Make sure that ``guild_id`` is a primary key.

5. Add three columns (guild_id, channel_name and channel_id) to the [requests-table](https://cdn.discordapp.com/attachments/771635939700768769/827459186870190100/unknown.png). **We do not need a primary key here!**

6. Start the bot and type ``?ticket`` in your ticket-channel. A message [like](https://cdn.discordapp.com/attachments/771635939700768769/827460503185653790/unknown.png) this should pop up.

7. Now copy the ID of your server and the message you just created and fill it in the database. Your DB should look like [this](https://cdn.discordapp.com/attachments/771635939700768769/827460984628183060/unknown.png).

---------------------------------------------------------------------------------------------------------------------------------------------------------------------
```python

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

```
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

**ALSO dont forget to change the authors name to the name of your bot!**

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

9. Restart the bot and klick on 📩  - it should look like [this](https://cdn.discordapp.com/attachments/771635939700768769/798487685471797328/unknown.png)

You have three diffrent emoji choices:

✅ -> Claim the ticket ([example](https://cdn.discordapp.com/attachments/771635939700768769/798489702093029376/unknown.png)) (*The creator of the ticket cant claim it*)

⛔ -> Mention every supporter ([example](https://cdn.discordapp.com/attachments/771635939700768769/798487939063087133/unknown.png))

🔒 -> Close the ticket - channel will delete itself after 10 seconds ([example](https://cdn.discordapp.com/attachments/771635939700768769/798488068038328330/unknown.png))

**After closing the ticket it will no longer be accessable**

# Done

If you did everything correctly the bot should work like in the examples!

Still questions? Join my [discord server](https://discord.gg/WRH22qat76)

(I will not reply to E-Mails)
