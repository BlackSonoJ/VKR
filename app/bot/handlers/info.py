from telegram import Update
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.error import BadRequest
from telegram.ext import (
    CallbackQueryHandler,
    ContextTypes,
)


async def __info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = "Информация"
    reply_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Назад", callback_data="start")],
        ]
    )

    try:
        query = update.callback_query
        await query.answer()
        await query.edit_message_text(
            text=text,
            reply_markup=reply_markup,
        )
    except BadRequest:
        await update.message.reply_text(
            text=text,
            reply_markup=reply_markup,
        )


def info_cbq_handler_main(pattern: str) -> CallbackQueryHandler:
    return CallbackQueryHandler(__info, pattern=pattern)
