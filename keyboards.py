from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from db import get_brends, get_phones_by_brend
from pprint import pprint


def home_keyboard():
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton('🛍 Shop'), KeyboardButton('🛒 Cart')],
            [KeyboardButton('ℹ️ About'), KeyboardButton('☎️Contact')],
        ],
        resize_keyboard=True,
    )

def brends_keyboard():
    keyboards_btns = []
    row = []
    for brend in get_brends():
        row.append(InlineKeyboardButton(brend, callback_data=f'brend:{brend}'))
        if len(row) == 2:
            keyboards_btns.append(row)
            row = []

    if row:
        keyboards_btns.append(row)

    return InlineKeyboardMarkup(
        keyboards_btns
    )

def phones_keyboard(brend: str):
    phones = get_phones_by_brend(brend=brend)
    keyboard_btns = []
    for phone in phones:
        btn = InlineKeyboardButton(
            text=phone['name'],
            callback_data=f'phone:{brend}-{phone.doc_id}'

        )
        keyboard_btns.append([btn])
    return InlineKeyboardMarkup(
        keyboard_btns
    )