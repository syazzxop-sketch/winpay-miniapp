from telegram import Update
from telegram.ext import ContextTypes

from keyboards import (
    main_menu,
    deposit_menu,
    payment_menu,
    bonus_menu,
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["waiting_code"] = True

    await update.message.reply_text(
        "🎉 *Welcome!*\n\n"
        "🔑 Please Enter Your *Invitation Code*",
        parse_mode="Markdown",
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    # Invitation Code
    if context.user_data.get("waiting_code"):
        context.user_data["waiting_code"] = False

        await update.message.reply_text(
            "✅ *Invitation Code Verified Successfully!*\n\n"
            "💎 Welcome to *WinPay*.\n\n"
            "👇 Please choose an option below.",
            parse_mode="Markdown",
            reply_markup=main_menu(),
        )
        return

    # ==========================
    # Deposit Menu
    # ==========================

    if text == "⚡ Deposit (UPI)":

        await update.message.reply_text(
            "💰 *Select Deposit Amount*",
            parse_mode="Markdown",
            reply_markup=deposit_menu(),
        )

    elif text in [
        "✅ ₹500",
        "✅ ₹1000",
        "✅ ₹2000",
    ]:

        if text == "✅ ₹500":
            bonus = "🎁 ₹598"

        elif text == "✅ ₹1000":
            bonus = "🎁 ₹1198"

        else:
            bonus = "🎁 ₹2398"

        await update.message.reply_text(
            f"""💰 *Deposit {text.replace("✅ ","")}*

{bonus}

🏦 *UPI ID*

`mikacswinpay-1@oksbi`

━━━━━━━━━━━━━━

1️⃣ Pay Using UPI

2️⃣ Send Payment Screenshot

✅ Balance Added After Verification
""",
            parse_mode="Markdown",
            reply_markup=payment_menu(),
        )

    # ==========================
    # Bonus Offers
    # ==========================

    elif text == "🎁 Bonus Offers":

        await update.message.reply_text(
            """🎉 *WINPAY BONUS OFFERS*

━━━━━━━━━━━━━━

✅ ₹500   ➜   🎁 ₹598
✅ ₹1000 ➜   🎁 ₹1198
✅ ₹2000 ➜   🎁 ₹2398

━━━━━━━━━━━━━━

⚡ Fast • 🔒 Secure • 💎 Trusted
""",
            parse_mode="Markdown",
            reply_markup=bonus_menu(),
        )

    # ==========================
    # Premium
    # ==========================

    elif text == "💎 Premium":

        await update.message.reply_text(
            "💎 *Premium*\n\n🚧 Coming Soon...",
            parse_mode="Markdown",
        )

    # ==========================
    # How To Deposit
    # ==========================

    elif text == "📖 How To Deposit":

        await update.message.reply_text(
            """📖 *HOW TO DEPOSIT*

① Click Deposit (UPI)

② Select Amount

③ Pay Using UPI

④ Send Payment Screenshot

⑤ Balance Added After Verification ✅

⚡ Fast • 🔒 Secure • 💎 Trusted
""",
            parse_mode="Markdown",
        )

    # ==========================
    # Customer Support
    # ==========================

    elif text == "🎧 Customer Support":

        await update.message.reply_text(
            """🎧 *Customer Support*

━━━━━━━━━━━━━━

👤 Support Team

👉 @miss_ArjaliWS

⏱ Reply Time
5–15 Minutes

📸 Please send your payment screenshot after deposit.
""",
            parse_mode="Markdown",
        )

    # ==========================
    # Send Screenshot
    # ==========================

    elif text == "📤 Send Screenshot":

        await update.message.reply_text(
            "📸 Please send your payment screenshot.\n\n⏱ Verification Time: 1–10 Minutes"
        )

    # ==========================
    # Back
    # ==========================

    elif text == "⬅️ Back":

        await update.message.reply_text(
            "🏠 *Main Menu*",
            parse_mode="Markdown",
            reply_markup=main_menu(),
        )

    else:

        await update.message.reply_text(
            "❌ Invalid option.\n\nPlease choose an option from the menu.",
            reply_markup=main_menu(),
        )