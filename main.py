import asyncio
import json
import os
import sys
import time
from telethon import TelegramClient, functions, types
from telethon.errors import RPCError
import config

PROCESSED_GIFTS_FILE = 'proc_gifts.json'

BANNER = r"""
    __  ______    __    _____   ______ _       _______ __ __ ____
   /  |/  /   |  / /   /  _/ | / / __ \ |     / / ___// //_//  _/
  / /|_/ / /| | / /    / //  |/ / / / / | /| / /\__ \/ ,<   / /  
 / /  / / ___ |/ /____/ // /|  / /_/ /| |/ |/ /___/ / /| |_/ /  
/_/  /_/_/  |_/_____/___/_/ |_/\____/ |__/|__//____/_/ |_/___/  
"""

class GiftUpgrader:
    def __init__(self, client):
        self.client = client
        self.processed_ids, file_existed = self.load_processed_gifts()
        self.is_initial_run = not file_existed

    def load_processed_gifts(self):
        if not os.path.exists(PROCESSED_GIFTS_FILE):
            return set(), False
        try:
            with open(PROCESSED_GIFTS_FILE, 'r', encoding='utf-8') as f:
                return set(json.load(f)), True
        except (json.JSONDecodeError, FileNotFoundError):
            return set(), False

    def save_processed_gifts(self):
        with open(PROCESSED_GIFTS_FILE, 'w', encoding='utf-8') as f:
            json.dump(list(self.processed_ids), f)

    async def log(self, msg):
        print(msg, flush=True)
        if config.LOG_CHAT:
            try:
                await self.client.send_message(config.LOG_CHAT, msg)
            except Exception:
                pass

    async def run_once(self):
        res = await self.client(functions.payments.GetStarGiftsRequest(hash=0))
        new_gift_found = False
        current_run_new_ids = []

        for gift in res.gifts:
            if gift.upgrade_stars is not None and gift.id not in self.processed_ids:
                if not self.is_initial_run:
                    message = (
                        f"**New gift get upgrade**\n\n"
                        f"**{gift.title}** -> t.me/nft/{gift.title.replace(' ', '')}-1\n"
                        f"**Price: {gift.upgrade_stars}**⭐️"
                    )
                    await self.client.send_message(config.TARGET_CHANNEL, message)
                
                current_run_new_ids.append(gift.id)
                new_gift_found = True

        if new_gift_found:
            self.processed_ids.update(current_run_new_ids)
            self.save_processed_gifts()

        self.is_initial_run = False

    async def loop(self):
        print(BANNER)
        while True:
            try:
                await self.run_once()
            except asyncio.TimeoutError:
                await self.log("Cycle timeout")
            except Exception as e:
                await self.log(f"Cycle error: {repr(e)}")
            
            await asyncio.sleep(config.CHECK_INTERVAL_SECONDS)

async def amain():
    client = TelegramClient(config.SESSION, config.API_ID, config.API_HASH)
    await client.start()
    upgrader = GiftUpgrader(client)
    await upgrader.loop()

if __name__ == "__main__":
    try:
        asyncio.run(amain())
    except KeyboardInterrupt:
        sys.exit(0)

