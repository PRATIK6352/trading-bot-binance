import streamlit as st
import pandas as pd
import traceback

from bot.orders import (
    place_market_order,
    place_limit_order,
    get_order_history,
    get_account_balance
)

st.set_page_config(page_title="Trading Bot", layout="wide")

st.title("📈 Binance Futures Trading Bot (Testnet)")
st.markdown("Mini Trading Dashboard")

# =============================
# ORDER PLACEMENT SECTION
# =============================

st.header("🛒 Place Order")

col1, col2 = st.columns(2)

with col1:
    symbol = st.text_input("Symbol", value="BTCUSDT").upper()
    side = st.selectbox("Side", ["BUY", "SELL"])
    order_type = st.radio("Order Type", ["MARKET", "LIMIT"])
    quantity = st.text_input("Quantity", value="0.002")
    quantity = round(float(quantity), 3)

with col2:
    price = None
    if order_type == "LIMIT":
        price = st.text_input("Limit Price",placeholder="USDT")

if st.button("Place Order"):
    try:
        if order_type == "MARKET":
            order = place_market_order(symbol, side, quantity)
        else:
            order = place_limit_order(symbol, side, quantity, price)

        st.success("Order placed successfully!")

        st.json(order)

    except ValueError as ve:
        st.warning(str(ve))  # user input / notional errors

    except Exception as e:
        st.error("Unexpected error occurred.")
        st.error(str(e))


# =============================
# ORDER HISTORY SECTION
# =============================

st.header("📜 Recent Order History")

try:
    orders = get_order_history(symbol)

    if orders:
        df = pd.DataFrame(orders)
        df = df[["orderId", "type", "side", "status", "origQty", "executedQty", "avgPrice", "updateTime"]]
        st.dataframe(df)
    else:
        st.info("No recent orders")

except Exception:
    st.error("Failed to fetch order history")


# =============================
# BALANCE SECTION
# =============================

st.header("💵 USDT Balance")

try:
    balance = get_account_balance()
    if balance:
        st.json({
            "Total Balance": balance["balance"],
            "Available Balance": balance["availableBalance"]
        })
    else:
        st.info("Balance not found")

except Exception:
    st.error("Failed to fetch balance")