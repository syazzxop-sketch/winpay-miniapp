import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "8951981980:AAHHSrhbH0c-hEBAqUe4iTbooyh6CxnUkGM")
UPI_ID = os.getenv("UPI_ID", "mikacswinpay-1@oksbi")
SUPPORT_USERNAME = os.getenv("SUPPORT_USERNAME", "@miss_AnjaliWS")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME", "https://t.me/+b3fW6Gkqpv9kOTh1")

APP_NAME = "WinPay"