from telegram import Update
from telegram.ext import ContextTypes

from keyboards import (
    main_menu,
    deposit_menu,
    payment_menu,
    bonus_menu,
)

from config import UPI_ID, SUPPORT_USERNAME


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["waiting_code"] = True

    await update.message.reply_text(
        "🎉 *WINPAY mein aapka swagat hai!* 💚\n\n"
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
    ]:

        if text == "✅ ₹500":
            bonus = "🎁 +₹98"

        elif text == "✅ ₹1000":
            bonus = "🎁 +₹198"

        else:
            bonus = "🎁 +₹298"

        await update.message.reply_text(
            f"""💰 *Deposit : {text.replace("✅ ", "")}*

{bonus}

🏦 *UPI ID*

`{UPI_ID}`

1️⃣ Pay Using UPI

2️⃣ Send Payment Screenshot

3️⃣ Balance Added After Verification ✅
""",
            parse_mode="Markdown",
            reply_markup=payment_menu(),
        )

    # =========================
    # Bonus Offers
    # =========================

    elif text == "🎁 Bonus Offers":

        await update.message.reply_text(
            """🎉 *WINPAY Bonus Offers* 🎊

✅ Deposit ₹500  → Get ₹598

✅ Deposit ₹1000 → Get ₹1198

✅ Deposit ₹2000 → Get ₹2298

💚 Bonus is added after successful payment. ✅
""",
            parse_mode="Markdown",
            reply_markup=bonus_menu(),
        )

    # =========================
    # Premium
    # =========================

    elif text == "💎 Premium":

        await update.message.reply_text(
            """💎 *WINPAY Premium*

⭐ Fast Verification

⭐ Priority Support

⭐ Exclusive Offers

📞 Contact support to activate Premium.
""",
            parse_mode="Markdown",
        )

    # =========================
    # How To Deposit
    # =========================

    elif text == "📖 How To Deposit":

        await update.message.reply_text(
            """📖 *How To Deposit*

1️⃣ Click **Deposit (UPI)**

2️⃣ Select Deposit Amount

3️⃣ Pay using the given UPI ID

4️⃣ Click **Send Screenshot**

5️⃣ Wait for verification (1–10 Minutes) ✅
""",
            parse_mode="Markdown",
        )

    # =========================
    # Customer Support
    # =========================

    elif text == "🎧 Customer Support":

        await update.message.reply_text(
            f"""🎧 *Customer Support*

━━━━━━━━━━━━━━

👤 Support Team

👉 {SUPPORT_USERNAME}

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
            """📤 *Send Payment Screenshot*

✅ Please send your payment screenshot here.

⏰ Verification Time:
1–10 Minutes
""",
            parse_mode="Markdown",
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

