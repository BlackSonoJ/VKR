from telegram import Update
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler,
)


def __markup_media_start() -> InlineKeyboardMarkup:

    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "Статистика",
                    callback_data="stats",
                )
            ],
            [
                InlineKeyboardButton(
                    "Информация",
                    callback_data="info",
                )
            ],
            [
                InlineKeyboardButton(
                    "Закрыть",
                    callback_data="close",
                )
            ],
        ]
    )


async def __start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = "Первая страница"
    reply_markup = __markup_media_start()

    try:
        query = update.callback_query
        await query.answer()
        await query.edit_message_text(
            text=text,
            reply_markup=reply_markup,
        )
    except AttributeError:
        await update.message.reply_text(
            text=text,
            reply_markup=reply_markup,
        )


def start_command_handler(command: str) -> CommandHandler:
    return CommandHandler(command, __start)


def start_cbq_handler(pattern: str) -> CallbackQueryHandler:
    return CallbackQueryHandler(__start, pattern=pattern)
