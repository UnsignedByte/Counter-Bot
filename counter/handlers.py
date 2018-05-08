# Add modules here
import discord

import asyncio

async def on_message(Counter, msg):
    try:
        async for a in Counter.logs_from(msg.channel, limit=1, before=msg):
            if int(msg.content) != int(a.content)+1 or msg.content.startswith('0'):
                await Counter.delete_message(msg)
    except ValueError:
        await Counter.delete_message(msg)
