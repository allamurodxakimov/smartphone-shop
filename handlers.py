from telegram import Update
from telegram.ext import CallbackContext
import keyboards
from db import get_phone_by_id


def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    update.message.reply_text(
        text=f"""
        Assalomu alaykum {user.full_name.capitalize()}
Telfon buyurtma berish uchun bizga Mahsulot nomini va Ism familiyangiz, telefon raqamingiz hamda yashash manzilingizni toʻliq yozib yuboring! 

Admin sizga 24 soat ichida jabov yozadi

🔥 Barcha mahsulotlar: @allamurod_2806
""",
        reply_markup=keyboards.home_keyboard()
    )

def shop(update: Update, context: CallbackContext):
    user = update.message.from_user
    update.message.reply_text(
        text=f'{user.full_name.capitalize()} Start Shopping 🔥',
        reply_markup=keyboards.brends_keyboard()
    )

def phones(update: Update, context: CallbackContext):
    brend = update.callback_query.data.split(":")[1]

    update.callback_query.message.reply_text(
        text=f'Start Shopping 🔥',
        reply_markup=keyboards.phones_keyboard(brend)
    )

def phone(update: Update, context: CallbackContext):
    brend,phone_id = update.callback_query.data.split(':')[1].split('-')

    # print(brend, phone_id)
    phone_data = get_phone_by_id(brend=brend.strip(), doc_id=phone_id.strip())
    # print(phone_data)
    update.callback_query.message.reply_photo(
        photo=phone_data['img_url'],
        caption=f'📲 {phone_data["name"]}\n🏪 {phone_data["company"]}\n{phone_data["color"]}\n{phone_data["RAM"]}\n{phone_data["memory"]}\n{phone_data["price"]}'

    )


def about(update: Update, context: CallbackContext):
    user = update.message.from_user
    update.message.reply_html(
        text=f"Salom Hurmatli {user.first_name}" + """

⚠️DIQQAT BU QONLANMANI OXIROGACHA OQING✅

Bu bot orqali siz xich qanday grupalarga odam qoshmastan? telefon  yutib olishingiz mumkun.
Uning uchun Ball toplash tugmasini bosasiz ☑️
Qachonki sizning balingiz 300Ball dan oshsa "Sovgalar" tugmasini bosing☑️
Va telefon sohibi boling📲✅.
Dostavka xizmati bor pullik💸
Tolovi oldindan amalga oshiriladi⏳✅.""",
        reply_markup=keyboards.home_keyboard()
    )

def contact(update: Update, context: CallbackContext):
    user = update.message.from_user
    update.message.reply_contact(
        phone_number="+998938554640",
        first_name=user.first_name,
        reply_markup=keyboards.home_keyboard()
    )
