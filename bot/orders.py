import logging
import time
from bot.client import get_client


def place_market_order(symbol, side, quantity):
    check_min_notional(symbol, quantity)
    client = get_client()

    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        time.sleep(2)  # wait for execution update

        order_status = client.futures_get_order(
            symbol=symbol,
            orderId=order["orderId"]
        )

        logging.info(f"Market order placed: {order_status}")
        return order_status

    except Exception as e:
        logging.error(f"Market order failed: {str(e)}")
        raise


def place_limit_order(symbol, side, quantity, price):
    client = get_client()

    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logging.info(f"Limit order placed: {order}")
        return order

    except Exception as e:
        logging.error(f"Limit order failed: {str(e)}")
        raise

def check_min_notional(symbol, quantity):
    client = get_client()

    ticker = client.futures_symbol_ticker(symbol=symbol)
    current_price = float(ticker["price"])
    MIN_NOTIONAL = 100

    notional = current_price * float(quantity)
    if notional < MIN_NOTIONAL:
        required_qty = MIN_NOTIONAL / current_price
        raise ValueError(
            f"Minimum notional is 100 USDT.\n"
            f"Increase quantity to at least {required_qty:.4f}"
        )

def get_order_history(symbol):
    client = get_client()
    orders = client.futures_get_all_orders(symbol=symbol, limit=10)
    return orders

def get_account_balance():
    client = get_client()
    balance_info = client.futures_account_balance()

    for asset in balance_info:
        if asset["asset"] == "USDT":
            return asset

    return None