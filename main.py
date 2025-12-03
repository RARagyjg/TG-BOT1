from instagrapi import Client
import time
import random
import requests

# -----------------------------
#        CONFIG
# -----------------------------
SESSIONID = "75694570387%3AkB9Z3WJFOP3uL5%3A14%3AAYiUw7HxmndT8xkTSGACv4FGkxbwtRyG9QywUmzSZg"
TARGET_THREAD_ID = "2859303934258963"  # GC ya DM thread id

TELEGRAM_BOT_TOKEN = "8421200250:AAENRgbY0KRlFG-6Q47mZu1Xt4-iLlFtQ54"
TELEGRAM_CHAT_ID = "8293933451"

SEND_MESSAGES = [
    """OMA/LAHIRU TERI RUNDY MAIYA KE MUH MEI LND DALKR MUTH MARUNGA💋💦-----------------------------------------------------------------------------------------------------------------------------------------------OMA/LAHIRU KI BEHN KE MUH MEI PESAB KARUNGA--------------------------------------------------------------------------------------------OMA/LAHIRU TERI RUNDY MAIYA KE MUH MEI LND DALKR MUTH MARUNGA💋💦----------------------------------------------------------------------------------------------------------------------------------------------OMA/LAHIRU KI BEHN KE MUH MEI PESAB KARUNGA--------------------------------------------------------------------------------------------OMA/LAHIRU TERI MAKI  XHUT MARUNGA KUTIYA KE B33EJJ""",
    """AJ TERYY MA KI CH00T FAD DUGA🖤








BHAG MATT TU BETE 🖤


TU CHOTA TATTA H BETE🖤



APNI MA CHUDA KE MANEGA🖤






 TERI MA AUJLA KE LND PE H🖤








 GRIB BHEEK DU BOL RNDI🖤











 GRIB TERI MAA CHUDA MERE SE🖤









OMA / SAM/ BLACK TERI MA CHOD KE PAISE DUNGA CHLEGA NA🥀 . """
]

SEND_DELAY = 60  # seconds (1 min)


# -----------------------------
#  TELEGRAM NOTIFICATION FUNCTION
# -----------------------------
def send_telegram(text):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        data = {"chat_id": TELEGRAM_CHAT_ID, "text": text}
        requests.post(url, data=data)
    except:
        pass


# -----------------------------
#       LOGIN INSTAGRAM
# -----------------------------
cl = Client()
cl.login_by_sessionid(SESSIONID)

print("🔥 Auto-Sender Bot Running (Render 24/7)")
send_telegram("🔥 Auto-Sender Bot Started Successfully!")


# -----------------------------
#         AUTO LOOP
# -----------------------------
while True:
    try:
        msg = random.choice(SEND_MESSAGES)

        # insta message send
        cl.direct_send(msg, [TARGET_THREAD_ID])

        log = f"[SENT] {msg}"
        print(log)

        # telegram notify
        send_telegram(f"📤 Message Sent:\n{msg}")

        time.sleep(SEND_DELAY)

    except Exception as e:
        error_msg = f"⚠️ Error: {e}"
        print(error_msg)
        send_telegram(error_msg)
        time.sleep(5)
