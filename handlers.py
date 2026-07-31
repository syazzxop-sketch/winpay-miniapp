from telegram import Update
from telegram.ext import ContextTypes

from keyboards import main_menu


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["waiting_code"] = True

    await update.message.reply_text(
        "🎉 *Welcome!*\n\n"
        "🔑 Please Enter Your *Invitation Code:*",
        parse_mode="Markdown"
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    # Invitation Code
    if context.user_data.get("waiting_code"):
        context.user_data["waiting_code"] = False

        await update.message.reply_text(
            "✅ *Success!*\n\n"
            "🎉 Invitation Code Verified Successfully.\n"
            "💎 Welcome to *WinPay*.\n\n"
            "👇 Please choose an option below.",
            parse_mode="Markdown",
            reply_markup=main_menu()
        )
        return

    # Deposit
    if text == "⚡ Deposit (UPI)":
        await update.message.reply_text(
            "⚡ *Deposit (UPI)*\n\n"
            "UPI ID:\n"
            "`winpay@upi`\n\n"
            "✅ Send Payment Screenshot to Customer Support.",
            parse_mode="Markdown"
        )

    # Bonus
    elif text == "🎁 Bonus Offers":
        await update.message.reply_text(
            """🎁 *WINPAY BONUS OFFERS*

━━━━━━━━━━━━━━━━

✅ ₹500   ➜   🎁 ₹625
✅ ₹1000  ➜   🎁 ₹1356
✅ ₹1500  ➜   🎁 ₹1751
✅ ₹2000  ➜   🎁 ₹2411
✅ ₹2500  ➜   🎁 ₹2806
✅ ₹3000  ➜   🎁 ₹3454
✅ ₹3500  ➜   🎁 ₹4009
✅ ₹4000  ➜   🎁 ₹4563
✅ ₹4500  ➜   🎁 ₹4987
✅ ₹5000  ➜   🎁 ₹5521

━━━━━━━━━━━━━━━━

🔥 Bonus credited after successful verification.

🔒 Safe • ⚡ Fast • 💯 Trusted
""",
            parse_mode="Markdown"
        )

    # Premium
    elif text == "💎 Premium":
        await update.message.reply_text(
            "💎 *Premium*\n\n🚧 Coming Soon...",
            parse_mode="Markdown"
        )

    # How to Deposit
    elif text == "📖 How To Deposit":
        await update.message.reply_text(
            """📖 *HOW TO DEPOSIT*

━━━━━━━━━━━━━━━━

① Click Deposit (UPI)

② Select Amount

③ Pay Using UPI

④ Send Payment Screenshot

⑤ Balance Added After Verification ✅

━━━━━━━━━━━━━━━━

⚡ Fast • 🔒 Secure • 💎 Trusted
""",
            parse_mode="Markdown"
        )

    # Customer Support
    elif text == "🎧 Customer Support":
        await update.message.reply_text(
            "@miss_AnjaliWS"
        )