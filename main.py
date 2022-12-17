import requests
import time
import json
# Glopal variables

api_key = 'd23a4124-1d50-479c-b025-584d8d7cfb34'
bot_key = '5817160291:AAHQ6Z7M74oG8p4Xr9WXYpNtnDkzE4T59ik'
chat_id = '985613710'
limit = 17000
time_interval = 5


def Get_price():
    url = "https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    parameters = {
        'start': 1,
        'limit': 100,
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'd23a4124-1d50-479c-b025-584d8d7cfb34',
    }
    response = requests.get(url, headers=headers, params=parameters).json()
    btc_price = response['data'][0]['quote']['USD']['volume_24h']  # ['price']
    return btc_price

def send_update(chat_id, msg):
    url = f"https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)

def main():
    while True:
        price = Get_price()
        print(price)
        if price < limit:
            send_update(chat_id, f"Price update = {price}")
        time.sleep(time_interval)

main()
