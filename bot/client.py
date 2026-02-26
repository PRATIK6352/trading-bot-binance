from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

def get_client():
    if not API_KEY or not API_SECRET:
        raise ValueError("API credentials not found in .env")

    # testnet=True ensures fake money environment
    return Client(API_KEY, API_SECRET, testnet=True)