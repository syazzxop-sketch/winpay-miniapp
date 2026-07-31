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
        "💎 *WINPAY main apka swagat hai 🔥*\n\n"
        "📝 *Please submit personal invitation code.*",
        parse_mode="Markdown"
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    # Invitation Code
    if context.user_data.get("waiting_code"):
        context.user_data["waiting_code"] = False

        await update.message.reply_text(
            "🎉 *Safal!*\n\n"
            "✅ System ne aapki jankari safalta se save kar li hai. \n",
            parse_mode="Markdown",
            reply_markup=main_menu()
        )
        return

    # Deposit
    # Deposit
if text == "⚡ Deposit (UPI)":
    await update.message.reply_text(
        "💰 *Select Deposit Amount*",
        parse_mode="Markdown",
        reply_markup=deposit_menu()
    )

elif text in [
    "🎁 ₹500+98",
    "🎁 ₹1000+198",
    "🎁 ₹2000+298",
    "🎁 ₹3000+398",
    "🎁 ₹4000+401",
    "🎁 ₹5000+505",
]:
    amount = text.replace("🎁 ", "")

    await update.message.reply_text(
        f"""🎁 *Deposit : {amount}*

🏦 UPI ID
`mikacswinpay-1@oksbi`

1️⃣ Pay the amount
2️⃣ Send Screenshot

✅ Balance Added After Verification
""",
        parse_mode="Markdown",
        reply_markup=payment_menu()
    )

    # Bonus
    elif text == "🎁 Bonus Offers":
        await update.message.reply_text(
            """🎉 *WINPAY Extra Bonus*

━━━━━━━━━━━━━━━━

✅ ₹500   ➜   🎁 ₹598
✅ ₹1000  ➜   🎁 ₹1198
✅ ₹1500  ➜   🎁 ₹1658
✅ ₹2000  ➜   🎁 ₹2298
✅ ₹2500  ➜   🎁 ₹2658
✅ ₹3000  ➜   🎁 ₹3398
✅ ₹3500  ➜   🎁 ₹3758
✅ ₹4000  ➜   🎁 ₹4401
✅ ₹4500  ➜   🎁 ₹4821
✅ ₹5000  ➜   🎁 ₹5505

━━━━━━━━━━━━━━━━

🔥 Bonus credited after successful verification.

🔒 Safe • ⚡ Fast • 💯 Trusted
""",
            parse_mode="Markdown"
        )

    # Premium
    elif text == "💎 Premium":
        await update.message.reply_text(
            "💎 *Premium*\n\n⏰ Coming Soon... 🙌🏻",
            parse_mode="Markdown"
        )

    # How to Deposit
    elif text == "📖 How To Deposit":
        await update.message.reply_text(
            """📖 *HOW TO DEPOSIT*

━━━━━━━━━━━━━━━━

1️⃣ Click Deposit (UPI)

2️⃣ Select Amount

3️⃣ Pay Using UPI

4️⃣ Send Payment Screenshot

5️⃣ Balance Added After Verification ✅

━━━━━━━━━━━━━━━━

⚡ Fast • 🔒 Secure • 💎 Trusted
""",
            parse_mode="Markdown"
        )

    # Customer Support
    elif text == "🎧 Customer Support":
        await update.message.reply_text(
"""🎧 *Customer Support*

━━━━━━━━━━━━━━

👤 Support Team

👉 @miss_AnjaliWS

⏰ Reply Time
5–15 Minutes

🙏 Please send your payment screenshot after deposit.
""",
parse_mode="Markdown"
)

elif text == "📤 Send Screenshot":
    await update.message.reply_text(
        "📸 Please send your payment screenshot.\n\nVerification Time : 1-10 Minutes"
    )
elif text == "⬅️ Back":
    await update.message.reply_text(
        "🏠 Main Menu",
        reply_markup=main_menu()
    )