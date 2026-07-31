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
        "🎉 WINPAY mein aapka swagat hai! 🔥\n\n"
        "📝 Please enter your invitation code.",
        parse_mode="Markdown",
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    # Invitation Code
    if context.user_data.get("waiting_code"):
        context.user_data["waiting_code"] = False

        await update.message.reply_text(
            """🎉 *Safal!*

✅ System ne aapka invitation code verify kar liya hai.

👇 Kripya niche se ek option chune.
""",
            parse_mode="Markdown",
            reply_markup=main_menu(),
        )
        return

    # =========================
    # Deposit
    # =========================

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
        "✅ ₹2500",
    ]:

        if text == "✅ ₹500":
            bonus = "🎁 +₹98"

        elif text == "✅ ₹1000":
            bonus = "🎁 +₹198"

        elif text == "✅ ₹2000":
            bonus = "🎁 +₹298"

        else:
            bonus = "🎁 +₹398"

        await update.message.reply_text(
            f"""💰 *Deposit : {text.replace("✅ ","")}*
{bonus}

🏦 *UPI ID*
`mikacswinpay-1@oksbi`

1️⃣ Pay Using UPI

2️⃣ Send Payment Screenshot

3️⃣ Balance Added After Verification ✅
""",
            parse_mode="Markdown",
            reply_markup=payment_menu(),
        )



    # =========================
    # Customer Support
    # =========================

    elif text == "🎧 Customer Support":

        await update.message.reply_text(
            """🎧 *Customer Support*

━━━━━━━━━━━━━━

👤 Support Team

👉 @miss_AnjaliWS

⏰ Reply Time:
5–15 Minutes

📥 Payment karne ke baad screenshot yahin bheje.
""",
            parse_mode="Markdown",
        )

    # =========================
    # Send Screenshot
    # =========================

    elif text == "📤 Send Screenshot":

        await update.message.reply_text(
            """📥 Please send your payment screenshot.

⏰ Verification Time: 1–10 Minutes""",
        )

    # =========================
    # Back
    # =========================

    elif text == "⬅️ Back":

        await update.message.reply_text(
            "🏠 *Main Menu*",
            parse_mode="Markdown",
            reply_markup=main_menu(),
        )

    # =========================
    # Invalid Option
    # =========================

    else:

        await update.message.reply_text(
            "❌ Invalid option.\n\nPlease choose an option from the menu.",
            reply_markup=main_menu(),
        )