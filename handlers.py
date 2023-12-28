from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext
import keyboards
from db import get_phone_by_id, add_item, get_items,clear_items

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
        text = f"{user.full_name} start Shopping 🔥",
        reply_markup=keyboards.brends_keyboard()
    )

def cart(update: Update, context: CallbackContext):
    user = update.effective_user
    items = get_items(user_id= user.id)
    text = "Your basket\n\n"
    total = 0
    for item in items:
        brend = item['brend']
        phone_id = item['phone_id'][0]
        # print(brend, phone_id)
        phone = get_phone_by_id(brend= brend, doc_id= phone_id)
        total += phone['price']

        text += f"#{phone.doc_id} {phone['name']} - {phone['price']} ming so'm\n"

    text += f"\nTotal : {total} ming so'm"
    update.message.reply_text(
        text= text,
        reply_markup= InlineKeyboardMarkup(
            [ 
                [InlineKeyboardButton('buy', callback_data= 'buy'), InlineKeyboardButton('clear', callback_data= 'clear-baskent')],
                [InlineKeyboardButton('close', callback_data= "close-baskent")]
            ]
        )
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
        caption=f'📲 {phone_data["name"]}\n🏪 {phone_data["company"]}\n🎨 {phone_data["color"]}\n💾 {phone_data["RAM"]}\n💽 {phone_data["memory"]}\n💰 {phone_data["price"]} ming so\'m',
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🛒 Add Cart",callback_data=f"add:{brend}-{phone_id}"),
                 InlineKeyboardButton("❌ Close", callback_data="close"),
                ]
            ]
        )
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

def close_phone(update: Update, context: CallbackContext):
    update.callback_query.message.delete()

def add_cart(update: Update, context: CallbackContext):
    user = update.effective_user
    brend, phone_id = update.callback_query.data.split(':')[1].split('-')
    print(brend, phone_id)
    add_item(user.id, brend.strip(), phone_id.split())

    update.callback_query.answer(text='Added item', show_alert=True)

def clear_basket(update: Update, context: CallbackContext):
    user = update.effective_user

    clear_items(user.id)

    update.callback_query.answer(
        text="Removed items",
        show_alert=True
    )
    close_phone(update,context)

def buy_basket(update: Update, context: CallbackContext):
    user = update.effective_user
    update.callback_query.answer(
        text="Buy items",
        show_alert=True
    )
    update.callback_query.message.reply_text(
        text=f"{user.full_name.capitalize()} sizning xaridingiz muvaffaqiyatli amalga oshirildi ✅.\nMahsulotlaringizni qabul qilish uchun poshta xizmatlarimiz bilan bog'laning 👉 @allamurod_2806",
        reply_markup= keyboards.home_keyboard()
    )