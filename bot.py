from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,CallbackQueryHandler
from config import get_token
import handlers


def main():
    TOKEN = get_token()

    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', handlers.start))
    dp.add_handler(MessageHandler(Filters.text('🛍 Shop'), handlers.shop))
    dp.add_handler(MessageHandler(Filters.text("ℹ️ About"),handlers.about))
    dp.add_handler(MessageHandler(Filters.text("☎️Contact"), handlers.contact))
    dp.add_handler(MessageHandler(Filters.text("🛒 Cart"), handlers.cart))

    dp.add_handler(CallbackQueryHandler(handlers.phones, pattern="brend:"))
    dp.add_handler(CallbackQueryHandler(handlers.phone, pattern="phone:"))
    dp.add_handler(CallbackQueryHandler(handlers.close_phone, pattern='close'))
    dp.add_handler(CallbackQueryHandler(handlers.add_cart, pattern="add:"))
    dp.add_handler(CallbackQueryHandler(handlers.clear_basket, pattern='clear'))
    dp.add_handler(CallbackQueryHandler(handlers.buy_basket, pattern="buy"))
    
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
