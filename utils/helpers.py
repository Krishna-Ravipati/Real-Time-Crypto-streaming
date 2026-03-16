import time
import requests

def fetch_crypto_price():
    """
    Fetches live Bitcoin and Ethereum prices in USD using CoinGecko API.
    """
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data:", response.status_code)
        return None

def wait(seconds):
    """
    Simple wrapper for time.sleep
    """
    time.sleep(seconds)