import argparse
from bot.logging_config import setup_logging
from bot.validators import *
from bot.orders import *


def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True, help="e.g. BTCUSDT")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, help="Order quantity")
    parser.add_argument("--price", required=False, help="Required for LIMIT order")
    parser.add_argument("--stop-price", required=False, help="Required for STOP-LIMIT order")

    args = parser.parse_args()

    try:
        # ---------- Validation ----------
        validate_side(args.side)
        if args.type not in ["MARKET", "LIMIT", "STOP"]:
            raise ValueError("Order type must be MARKET, LIMIT, or STOP")
        validate_quantity(args.quantity)

        # ---------- Place Order ----------
        if args.type == "MARKET":
            order = place_market_order(
                args.symbol,
                args.side,
                args.quantity
            )

        elif args.type == "LIMIT":
            validate_price(args.price)

            order = place_limit_order(
                args.symbol,
                args.side,
                args.quantity,
                args.price
            )
        elif args.type == "STOP":
            validate_stop_price(args.stop_price)

            order = place_stop_order(
                args.symbol,
                args.side,
                args.quantity,
                args.stop_price
            )

        print("\n====== ORDER DETAILS ======")
        print("Order ID      :", order.get("orderId"))
        print("Symbol        :", order.get("symbol"))
        print("Side          :", order.get("side"))
        print("Type          :", order.get("type"))
        print("Status        :", order.get("status"))
        print("Executed Qty  :", order.get("executedQty"))
        print("Avg Price     :", order.get("avgPrice"))
        print("============================\n")

    except Exception as e:
        import traceback
        print("\nFULL ERROR:")
        traceback.print_exc()


if __name__ == "__main__":
    main()