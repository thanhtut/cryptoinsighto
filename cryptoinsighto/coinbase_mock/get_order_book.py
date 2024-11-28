from .generate_mock_order_book import generate_mock_order_book


async def get_order_book(symbol: str = "BTC-USD", level: int = 2):
    # Simulate different cryptocurrencies with slight price variations
    price_map = {"BTC-USD": 71234.56, "ETH-USD": 3786.42, "SOL-USD": 178.23, "XRP-USD": 0.6123}

    # Validate symbol
    if symbol not in price_map:
        raise NotImplementedError
    if level != 2:
        raise NotImplementedError

    base_price = price_map[symbol]
    return generate_mock_order_book(symbol, base_price)
