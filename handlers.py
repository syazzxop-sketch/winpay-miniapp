elif text == "🎁 Post & Share ₹17-177":
    await update.message.reply_text(
        """
🎁 *POST & SHARE*

🚧 Coming Soon...

✨ Next update me ye feature available hoga.

🎁 Reward: ₹17 - ₹177
""",
        parse_mode="Markdown"
    )

elif text == "🍀 Invite & Earn":
    await update.message.reply_text(
        """
🍀 *Invite & Earn*

🚧 Coming Soon...

Invite karke bonus earn kar paoge.
""",
        parse_mode="Markdown"
    )

elif text == "✨ WinPay Official Channel":
    await update.message.reply_text(
        f"📢 Join Official Channel:\n{CHANNEL_USERNAME}"
    )

elif text == "📱 How To Use App":
    await update.message.reply_text(
        """
📱 *How To Use App*

1️⃣ Deposit karo
2️⃣ Bonus claim karo
3️⃣ Play karo
4️⃣ Enjoy 🎉
""",
        parse_mode="Markdown"
    )

elif text == "💳 How To Deposit":
    await update.message.reply_text(
        f"""
💳 *Offline Deposit*

UPI ID:
`{UPI_ID}`

✅ Payment karne ke baad Customer Support ko screenshot bhej do.
""",
        parse_mode="Markdown"
    )

elif text == "💸 Withdrawal":
    await update.message.reply_text(
        """
💸 *Withdrawal*

🚧 Coming Soon...
""",
        parse_mode="Markdown"
    )