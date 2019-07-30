import discord
import asyncio
import logging

import counter.client.getkey as _getkey
import counter.handlers

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='data/discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

class CounterClient(discord.Client):
    async def on_ready(self):
        await self.change_presence(game=discord.Game(name='You Count', url='https://github.com/UnsignedByte/Counter-Bot', type=3))
    async def on_message(self, message):
        await counter.handlers.on_message(self, message)
    async def on_message_edit(self, before, after):
        await counter.handlers.on_message(self, after)
Counter = CounterClient()

def runBot():
    Counter.run(_getkey.key())

if __name__ == "__main__":
    print("Auth key is %s" % _getkey.key())
