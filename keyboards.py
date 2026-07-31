from telegram import ReplyKeyboardMarkup

# Main Menu
def main_menu():
    keyboard = [
        ["⚡ Deposit (UPI)", "🎁 Bonus Offers"],
        ["💎 Premium", "📖 How To Deposit"],
        ["🎧 Customer Support"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


# Deposit Amount Menu
def deposit_menu():
    keyboard = [
        ["💰 ₹100", "💰 ₹200"],
        ["💰 ₹500", "💰 ₹1000"],
        ["💰 ₹2000", "💰 ₹5000"],
        ["⬅️ Back"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


# Payment Menu
def payment_menu():
    keyboard = [
        ["📤 Send Screenshot"],
        ["🎧 Customer Support"],
        ["⬅️ Back"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


# Bonus Menu
def bonus_menu():
    keyboard = [
        ["⬅️ Back"],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)