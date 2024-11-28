from decimal import Decimal
import random


def generate_mock_order_book(
    market_symbol: str, base_price: Decimal, bids_num: int = 5, asks_num: int = 5, level: int = 2
) -> dict:
    """
    Returns a json string
    """
    if level != 2:
        raise NotImplementedError

    # Generate bids (buy orders)
    bids = []
    for i in range(bids_num):
        # random bids slightly more than base price
        price = base_price * (1 + (random.uniform(0.1, 10.0) * 0.0001))
        # Decreasing volume with some randomness
        size = round(random.uniform(0.1, 10.0) * (1 / (i + 1)), 4)
        num_orders = random.randint(1, 5)

        bids.append([round(price, 4), round(size, 4), num_orders])

    # Generate asks (sell orders)
    asks = []
    for i in range(asks_num):
        # random slightly more than base price
        price = base_price * (1 - (random.uniform(0.1, 10.0) * 0.0001))
        # Decreasing volume with some randomness
        size = round(random.uniform(0.1, 10.0) * (1 / (i + 1)), 4)
        # Random number of orders
        num_orders = random.randint(1, 5)

        asks.append([round(price, 2), round(size, 4), num_orders])

    # Sort bids descending, asks ascending
    bids.sort(key=lambda x: x[0], reverse=True)
    asks.sort(key=lambda x: x[0])

    sequence = random.randint(1000000, 9999999)

    return {"bids": bids, "asks": asks, "sequence": sequence}
