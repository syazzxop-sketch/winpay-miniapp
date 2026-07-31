from telegram import ReplyKeyboardMarkup

def home_keyboard():
    keyboard = [
        ["⚡ Deposit (UPI)", "🎁 Bonus Offers"],
        ["💎 Premium", "📖 How To Deposit"],
        ["🎧 Customer Support", "📢 Official Channel"],
        ["🎁 Post & Share ₹17–177", "⭐ VIP Benefits"]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder="✨ Select an option..."
    )