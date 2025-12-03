import time
from instagrapi import Client
from telebot import TeleBot

# =================== CONFIG ===================
SESSION_ID = "75694570387%3AkB9Z3WJFOP3uL5%3A14%3AAYh3cBJJqU2FrlXO3LNUW9oeJsug7JepWRo1CJAWlg"
THREAD_ID = "2859303934258963"   # GC ka real thread ID (string)
MESSAGE = "OMA KI MA MAA RND😎"          # GC me bhejna message
SEND_DELAY = 60                     # Seconds me interval

TG_BOT_TOKEN = "8421200250:AAENRgbY0KRlFG-6Q47mZu1Xt4-iLlFtQ54"
CHAT_ID = "8293933451"
# ============================================

# Telegram bot init
bot = TeleBot(TG_BOT_TOKEN)

# Instagram client init
cl = Client()
cl.login_by_sessionid(SESSION_ID)

bot.send_message(CHAT_ID, "✅ Instagram GC Auto-Bot Started Successfully!")

while True:
    try:
        # 1️⃣ Send message to GC
        cl.direct_send(MESSAGE, [THREAD_ID])
        print(f"Sent: {MESSAGE} to {THREAD_ID}")

        # 2️⃣ Notify Telegram
        bot.send_message(CHAT_ID, f"✅ Message sent successfully to GC: {THREAD_ID}")

        # 3️⃣ Wait before next send
        time.sleep(SEND_DELAY)

    except Exception as e:
        # 4️⃣ Error handling & notify
        print("Error:", e)
        bot.send_message(CHAT_ID, f"❌ Error occurred: {str(e)}")
        time.sleep(10)
