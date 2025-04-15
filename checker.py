import os
import requests
from telegram import Bot

URL = "https://foundationcourse.unipi.it/"

# GitHub Secrets'tan çekiyoruz
BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def main():
    # 1. En son kaydettiğimiz referans metni oku
    with open("reference_text.txt", "r", encoding="utf-8") as f:
        old_text = f.read().strip()

    # 2. Şu an siteden HTML içerik çek
    try:
        response = requests.get(URL, timeout=10)
# TEST AMACIYLA new_text'i zorla değiştir
new_text += "TEST_Icin_zorlama_degisim"
        new_text = response.text.strip()  # Tüm HTML
    except Exception as e:
        # Siteye ulaşamazsak bile Telegram'dan hata mesajı atmak isteyebilirsin
        send_telegram_message(f"Siteye erişilemiyor. Hata: {e}")
        return

    # 3. Karşılaştırma yap
    if new_text != old_text:
        # Fark var, Telegram'dan haber ver
        send_telegram_message("DİKKAT! Web sayfasında değişiklik tespit edildi.")
        # Not: Burada istersen otomatik olarak reference_text.txt güncelletebilirsin
        # Ama GitHub Action'da commit atmak biraz ek ayar ister.
        # Şimdilik sen manuel olarak reference_text.txt içeriğini güncelleyebilirsin.
    else:
        # Fark yok
        pass

def send_telegram_message(message):
    bot = Bot(token=BOT_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=message)

if __name__ == "__main__":
    main()
