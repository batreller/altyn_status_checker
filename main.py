import asyncio
import time

from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
from logging_config import *
import altyn
import config

client = TelegramClient("session", config.api_id, config.api_hash)
client.start()


async def main():
    while True:
        status = altyn.get_status()
        check_time = time.time()
        for _ in range(30):  # 30 delays for 10 second
            last_check = int(time.time() - check_time)

            if status == 504:  # does not work
                await client(UpdateProfileRequest(first_name=f"joni dap [ALTYN DOES NOT WORK, check bio]", about=f"ALTYN DOES NOT WORK (checked {last_check} seconds ago)"))
                logger.info(f"ALTYN DOES NOT WORK (checked {last_check} seconds ago)")

            elif status == 200 or status == 201 or status == 202:  # works
                await client(UpdateProfileRequest(first_name=f"joni dap [ALTYN WORKS, check bio]", about=f"ALTYN WORKS (checked {last_check} seconds ago)"))
                logger.info(f"ALTYN WORKS (checked {last_check} seconds ago)")
            else:
                logger.warning(F"UNKNOWN ALTYN STATUS - {status}")
                with open("logs.txt", "a") as f:
                    f.write(f"{status} UNKNOWN STATUS\n")

                await client(UpdateProfileRequest(first_name="joni dap check bio", about=f"UNKNOWN ALTYN STATUS, WILL BE FIXED SOON (status {status}) (checked {last_check} seconds ago)"))

            await asyncio.sleep(10)  # 10 seconds


if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())
