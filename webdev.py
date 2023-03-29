import telegram.ext

Token = "6273624009:AAGga9Xp2nr6-kVsUTs39Y8ZTialc2e3ink"

updater = telegram.ext.Updater("6273624009:AAGga9Xp2nr6-kVsUTs39Y8ZTialc2e3ink", update_queue=True)

dispatcher = updater.dispatcher

def start(update, context):
    update.message.reply_text("Hi, welcome to WebDep. Please type '/help' to load the commands.")

def help(update, context):
    update.message.reply_text("""
    /start -> Welcome to the channel
    /help -> This particular message
    /content -> Playlists of WebDep
    /Python -> The first tutorial video from Python playlist
    /C -> The first tutorial video from C playlist
    /Java -> The first tutorial video from Java playlist
    /contact -> Contact information
    """)

def content(update, context):
    update.message.reply_text("Here are the various playlists available: ")

def Python(update, context):
    update.message.reply_text("Link: https://youtu.be/_uQrJ0TkZlc")

def C(update, context):
    update.message.reply_text("Link: https://youtu.be/KJgsSFOSQv0")

def Java(update, context):
    update.message.reply_text("Link: https://youtu.be/eIrMbAQSU34")

def contact(update, context):
    update.message.reply_text("Contact via registered mail id provided on the website.")

dispatcher.add_handler(telegram.ext.CommandHandler('help', help))
dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
dispatcher.add_handler(telegram.ext.CommandHandler('Python', Python))
dispatcher.add_handler(telegram.ext.CommandHandler('C', C))
dispatcher.add_handler(telegram.ext.CommandHandler('Java', Java))
dispatcher.add_handler(telegram.ext.CommandHandler('contact', contact))

updater.start_polling()
updater.idle()