import time
import requests

URL = "https://alx-backend-security-rn7o.onrender.com/"
INTERVAL = 600  # seconds (10 minutes)

def keep_awake():
    while True:
        try:
            r = requests.get(URL)
            print(f"Pinged {URL} - Status: {r.status_code}")
        except Exception as e:
            print(f"Error pinging {URL}: {e}")
        time.sleep(INTERVAL)

if __name__ == "__main__":
    keep_awake()
