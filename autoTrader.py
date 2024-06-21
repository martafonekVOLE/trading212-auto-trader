import dotenv
import os
import requests

MARKET_ORDER_URL = 'https://live.trading212.com/api/v0/equity/orders/market'

ARGUMENT_QUANTITY = 'quantity'
ARGUMENT_TICKER = 'ticker'


def buy_stock(symbol, quantity):
    dotenv.load_dotenv()

    parameters = {
        'symbol': symbol,
        'quantity': quantity,
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': os.getenv('API_KEY')
    }

    response = requests.post(MARKET_ORDER_URL, params=parameters, headers=headers)
