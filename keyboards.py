from telegram import ReplyKeyboardMarkup

def main_menu():
    keyboard = [
        ["⚡ Deposit (UPI)", "🎁 Bonus Offers"],
        ["💎 Premium", "📖 How To Deposit"],
        ["🎧 Customer Support"]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )