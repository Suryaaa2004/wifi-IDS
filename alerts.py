import requests
from datetime import datetime
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID, LOG_FILE, JSON_LOG_FILE
import json
import os

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": msg}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"[!] Telegram alert failed: {e}")

def alert(msg):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    full_msg = f"[ALERT] [{now}] {msg}"
    print(full_msg)
    send_telegram(full_msg)
    with open(LOG_FILE, "a") as f:
        f.write(f"{now},{msg}\n")
    entry = {"timestamp": now, "message": msg}
    if os.path.exists(JSON_LOG_FILE):
        with open(JSON_LOG_FILE, "r") as f:
            try:
                logs = json.load(f)
            except json.JSONDecodeError:
                logs = []
    else:
        logs = []
    logs.append(entry)
    with open(JSON_LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)
