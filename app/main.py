import logging
import os
import asyncio
from datetime import datetime

from telegram import Update
from telegram.ext import (
    Application,
)

from app.bot.handlers.start import start_command_handler, start_cbq_handler
from app.bot.handlers.info import info_cbq_handler_main
from app.bot.handlers.stats import stats_cbq_handler_main

# from app.collect_data import add_to_db

# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
# )
# logging.getLogger("httpx").setLevel(logging.WARNING)

# logger = logging.getLogger(__name__)


def main():
    application = Application.builder().token("token").build()

    application.add_handlers(
        handlers=[
            start_command_handler("start"),
            start_cbq_handler("start"),
            stats_cbq_handler_main("stats"),
            info_cbq_handler_main("info"),
        ]
    )

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    last_read = datetime.now()
    while True:
        now = datetime.now()
        if now.second % 5 == 0 and now.second != last_read.second:
            last_read = now
            print(datetime.now())
    # main()
    ...
