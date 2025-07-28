import os
import requests

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
USERNAMES = os.getenv("TELEGRAM_USERNAMES").split(",")

def send_message(message):
    for username in USERNAMES:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": f"@{username.strip()}", "text": message}
        requests.post(url, data=payload)

send_message("🚨 [SINYAL KUAT] SLP/IDR breakout! Potensi naik besar! 🎯")
