from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

import asyncio

try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())


def main():

    app = Application.builder().token(BOT_TOKEN).build()

    # Start Command
    app.add_handler(CommandHandler("start", start))

    # All Text Messages
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_message
        )
    )

    print("✅ WinPay Bot Started Successfully!")

    app.run_polling()


if __name__ == "__main__":
    main()