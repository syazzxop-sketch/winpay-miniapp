from telegram import ReplyKeyboardMarkup

def main_keyboard():
    keyboard = [
        ["💰 Deposit ( UPI )", "🎁 Bonus Offers"],
        ["👑 Premium Membership", "📖 How To Deposit (Offline)"],
        ["🎧 Customer Support", "📢 Official Channel"],
        ["👥 Invite & Earn", "💸 Withdrawal Process"],
        ["🛒 Purchase VIP Order", "📱 How To Use App"],
        ["🎉 Post & Share (Coming Soon)"]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        is_persistent=True,
        one_time_keyboard=False,
        input_field_placeholder="✨ Choose an option..."
    )