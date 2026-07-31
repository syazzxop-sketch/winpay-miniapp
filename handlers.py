from telegram import Update
from telegram.ext import ContextTypes

from keyboards import main_keyboard
from config import (
    APP_NAME,
    UPI_ID,
    SUPPORT_USERNAME,
    CHANNEL_USERNAME,
)


WELCOME_TEXT = f"""
👋 Welcome to {APP_NAME}

━━━━━━━━━━━━━━━━━━━━

🎉 Welcome to India's Fast Growing Platform

💎 Safe
⚡ Fast
🔒 Secure

👇 Select an option below.
"""


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        WELCOME_TEXT,
        reply_markup=main_keyboard()
    )


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "💰 Deposit":
        await update.message.reply_text(
"""
💰 SELECT DEPOSIT AMOUNT

━━━━━━━━━━━━━━━━━━━━

Choose your deposit amount.

💵 ₹500  → ₹625
💵 ₹1000 → ₹1356
💵 ₹1500 → ₹1751
💵 ₹2000 → ₹2411
💵 ₹2500 → ₹2806
💵 ₹3000 → ₹3454
💵 ₹3500 → ₹4009
💵 ₹4000 → ₹4563
💵 ₹4500 → ₹4987
💵 ₹5000 → ₹5521

👇 Amount selection next update me add hoga.
"""
)

    elif text == "📖 How To Deposit (Offline)":
        await update.message.reply_text(
f"""
📖 OFFLINE DEPOSIT GUIDE

1️⃣ Deposit button dabaye.

2️⃣ Amount choose kare.

3️⃣ UPI me payment kare.

UPI ID

{UPI_ID}

4️⃣ Screenshot bheje.

5️⃣ UTR Number bheje.

6️⃣ Verification ke baad balance credit hoga.
"""
)

    elif text == "🎁 Bonus Offers":
        await update.message.reply_text(
"""
🎁 Latest Bonus Offers

✅ Daily Bonus
✅ Deposit Bonus
✅ VIP Bonus

More offers coming soon...
"""
)

    elif text == "👑 Premium Membership":
        await update.message.reply_text(
"""
👑 Premium Membership

⭐ Fast Withdraw
⭐ Priority Support
⭐ VIP Benefits

Coming Soon...
"""
)

    elif text == "🎧 Customer Support":
        await update.message.reply_text(
f"Support: {SUPPORT_USERNAME}"
)

    elif text == "📢 Official Channel":
        await update.message.reply_text(
CHANNEL_USERNAME
)

    elif text == "👥 Invite & Earn":
        await update.message.reply_text(
"""
👥 Invite Friends

Invite your friends and earn rewards.

Coming Soon...
"""
)

    elif text == "💸 Withdrawal Process":
        await update.message.reply_text(
"""
💸 Withdrawal

Submit withdrawal request.

Processing time:
5-30 Minutes
"""
)

    elif text == "🛒 Purchase VIP Order":
        await update.message.reply_text(
"""
🛒 Purchase VIP

VIP Orders Coming Soon...
"""
)

    elif text == "📱 How To Use App":
        await update.message.reply_text(
"""
📱 Tutorial

Step 1 Login
Step 2 Deposit
Step 3 Start
Step 4 Withdraw
"""
)

    elif text == "🎉 Post & Share (Coming Soon)":
        await update.message.reply_text(
"🚧 Coming Soon..."
)