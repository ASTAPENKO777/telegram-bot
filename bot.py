from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters


user_states = {}
user_languages = {}

async def start(update: Update, context):
    user_id = update.message.from_user.id
    if user_id not in user_states:
        user_states[user_id] = "menu"  
        user_languages[user_id] = "uk" 
    await show_main_menu(update)

async def show_main_menu(update: Update):
    user_id = update.message.from_user.id
    lang = user_languages.get(user_id, "uk")
    if lang == "uk":
        keyboard = [
            ["📋 Прайс-лист", "📞 Контакти"],
            ["🌐 Ми в соцмережах", "🧑‍💼 Про мене"],
            ["🌐 Змінити мову"]
        ]
        message = "Ось моє меню. Оберіть потрібний розділ:"
    else:
        keyboard = [
            ["📋 Price List", "📞 Contacts"],
            ["🌐 Social Media", "🧑‍💼 About Me"],
            ["🌐 Change Language"]
        ]
        message = "Here is my menu. Choose a section:"
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(message, reply_markup=reply_markup)

async def show_social_media(update: Update):
    user_id = update.message.from_user.id
    lang = user_languages.get(user_id, "uk")
    message = (
        "🌐 Ми в соцмережах:\n\n"
        "Підписуйтеся на наші сторінки в соціальних мережах!"
        if lang == "uk" else
        "🌐 We are on social media:\n\n"
        "Follow our pages on social media!"
    )
    keyboard = [
        [
            InlineKeyboardButton("YouTube", url="https://youtube.com/@python_hub7777?si=aDDw15WAiXwKVaCv"),
            InlineKeyboardButton("Instagram", url="https://www.instagram.com/it.sites_development/?__pwa=1#"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(message, reply_markup=reply_markup)

async def change_language(update: Update):
    user_id = update.message.from_user.id
    lang = user_languages.get(user_id, "uk")
    keyboard = [
        ["Українська", "English"]
    ]
    message = (
        "Оберіть мову:" if lang == "uk"
        else "Choose a language:"
    )
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(message, reply_markup=reply_markup)

async def handle_message(update: Update, context):
    user_id = update.message.from_user.id
    text = update.message.text.strip().lower()
    lang = user_languages.get(user_id, "uk")
    print(f"Отримано повідомлення від користувача: {text}")
    if text in ["українська", "english"]:
        user_languages[user_id] = "uk" if text == "українська" else "en"
        await show_main_menu(update)
        return
    if text in ["📋 прайс-лист", "📋 price list"]:
        response = (
            "📋 **Прайс-лист:**\n\n"
            "1. Telegram-бот — від 3000 грн\n"
            "2. Сайт — від 5000 грн\n"
            "3. Додаток — від 8000 грн\n\n"
            "Для уточнення звертайтесь у розділі Контакти."
            if lang == "uk" else
            "📋 **Price List:**\n\n"
            "1. Telegram bot — from 3000 UAH\n"
            "2. Website — from 5000 UAH\n"
            "3. App — from 8000 UAH\n\n"
            "For details, refer to the Contacts section."
        )
        keyboard = [["↩️ Назад"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text(response, parse_mode='Markdown', reply_markup=reply_markup)
        return
    elif text in ["📞 контакти", "📞 contacts"]:
        response = (
            "📞 **Контакти:**\n\n- Київстар: +380 68 104 6228\n- Vodafone: +380 99 056 8454\n- Email one: kaktusbloog@gmail.com\n- Email two: kaktusbloog@ukr.net\n- Telegram: @astapenkko"
            if lang == "uk" else
            "📞 **Contacts:**\n\n- Kyivstar: +380 68 104 6228\n- Vodafone: +380 99 056 8454\n- Email one: kaktusbloog@gmail.com\n- Email two: kaktusbloog@ukr.net\n- Telegram: @astapenkko"
        )
        keyboard = [["↩️ Назад"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text(response, parse_mode='Markdown', reply_markup=reply_markup)
        return
    elif text in ["🧑‍💼 про мене", "🧑‍💼 about me"]:
        bio_text = (
            "🧑‍💼 **Про мене:**\n\n"
            "Мене звати Михайло, я розробник Telegram-ботів, Сайтів, Додатків. "
            "Моя мета — допомогти вам автоматизувати бізнес-процеси та створити сучасні цифрові рішення. "
            "Досвід: Вчуся в IT-school, спеціальність \"Python розробка\", + досвід у сферах розробки HTML, CSS, JS, SQL Lite.\n\n"
            "Зв'яжіться зі мною у розділі Контакти! 😊"
            if lang == "uk" else
            "🧑‍💼 **About Me:**\n\n"
            "My name is Mykhailo, and I am a developer of Telegram bots, Websites, and Applications. "
            "My goal is to help you automate business processes and create modern digital solutions. "
            "Experience: Studying at an IT school, specializing in Python development, with experience in HTML, CSS, JS, SQL Lite.\n\n"
            "Contact me via the Contacts section! 😊"
        )
        keyboard = [["↩️ Назад"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text(bio_text, parse_mode='Markdown', reply_markup=reply_markup)
        return
    elif text in ["🌐 змінити мову", "🌐 change language"]:
        await change_language(update)
        return
    elif text in ["🌐 ми в соцмережах", "🌐 social media"]:
        await show_social_media(update)
        return
    elif text == "↩️ назад":
        await show_main_menu(update)
        return
    response = "Невідомий вибір. Спробуйте ще раз." if lang == "uk" else "Unknown choice. Please try again."
    await update.message.reply_text(response, parse_mode='Markdown')

if __name__ == "__main__":
    TOKEN = "" # Введіть свій токен
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Бот запущено...")
    app.run_polling()
