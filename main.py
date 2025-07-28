import telegram
import time

TOKEN = "7247120688:AAHcEK1PP-stPq6YxgufILaSsI_ctasMwYc"
CHAT_IDS = ["@bam824", "@Clayfoor1789"]

bot = telegram.Bot(token=TOKEN)

def kirim_sinyal(pesan):
    for chat_id in CHAT_IDS:
        try:
            bot.send_message(chat_id=chat_id, text=pesan)
        except Exception as e:
            print(f"Gagal kirim ke {chat_id}: {e}")

if __name__ == "__main__":
    pesan = "🚨 [SINYAL PENTING] 1000CAT/IDR breakout kuat! Timeframe 15m 🚀"
    while True:
        kirim_sinyal(pesan)
        time.sleep(900)  # setiap 15 menit
