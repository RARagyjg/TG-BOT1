from instagrapi import Client
from telebot import TeleBot
import time

INSTAGRAM_SESSIONID = "75694570387%3AkB9Z3WJFOP3uL5%3A14%3AAYiUw7HxmndT8xkTSGACv4FGkxbwtRyG9QywUmzSZg"
TARGET_USER_ID = "2859303934258963"   # username nahi, ID
TELEGRAM_BOT_TOKEN = "8421200250:AAENRgbY0KRlFG-6Q47mZu1Xt4-iLlFtQ54"
TELEGRAM_CHAT_ID = "8293933451"

cl = Client()
tg = TeleBot(TELEGRAM_BOT_TOKEN)

# --- Login safely ---
cl.login_by_sessionid(INSTAGRAM_SESSIONID)

def send_telegram(text):
    try:
        tg.send_message(TELEGRAM_CHAT_ID, text)
    except Exception as e:
        print("Telegram Error:", e)

def send_message_loop():
    while True:
        try:
            text = "🔥 Auto Message by Bot"
            cl.direct_send(text, [int(TARGET_USER_ID)])
            send_telegram(f"✅ Message sent successfully: {text}")
            print("Sent:", text)
        except Exception as e:
            send_telegram(f"⚠️ Error:\n{e}")
            print("Error:", e)
        
        time.sleep(60)  # wait 1 min

if __name__ == "__main__":
    send_telegram(AJ TERYY MA KI CH00T FAD DUGA🖤








BHAG MATT TU BETE 🖤


TU CHOTA TATTA H BETE🖤



APNI MA CHUDA KE MANEGA🖤






 TERI MA RAHUL KE LND PE H🖤








 GRIB BHEEK DU BOL RNDI🖤











 GRIB TERI MAA CHUDA MERE SE🖤









OMA / SAM/ BLACK TERI MA CHOD KE PAISE DUNGA CHLEGA NA🥀 . )
    send_message_loop()
