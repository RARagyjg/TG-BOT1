import time
from instagrapi import Client
from telebot import TeleBot

SESSION_ID = "75694570387%3AkB9Z3WJFOP3uL5%3A14%3AAYh3cBJJqU2FrlXO3LNUW9oeJsug7JepWRo1CJAWlg"
THREAD_ID = "2859303934258963"   # <-- GC ka real thread id
MESSAGE = """OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  """
SEND_DELAY = 60

TG_BOT_TOKEN = "8421200250:AAENRgbY0KRlFG-6Q47mZu1Xt4-iLlFtQ54"
CHAT_ID = "8293933451"

bot = TeleBot(TG_BOT_TOKEN)
cl = Client()

cl.login_by_sessionid(SESSION_ID)

while True:
    try:
        # ⭐ GC message method
        cl.direct_send_to_thread(THREAD_ID, MESSAGE)

        bot.send_message(CHAT_ID, f"Message sent successfully to GC: {THREAD_ID}")
        print("Sent:", MESSAGE)

        time.sleep(SEND_DELAY)

    except Exception as e:
        bot.send_message(CHAT_ID, f"❌ Error: {str(e)}")
        print("Error:", e)
        time.sleep(10)
