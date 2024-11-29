import pandas as pd
from .run_analysis_wrapper import run_analysis
from typing import List
from cryptoinsighto.types.order_book_entry import OrderBookEntry
from decimal import Decimal

ANALYSIS_NAME = "max_spread"


@run_analysis(ANALYSIS_NAME)
def run_analysis(book_record_dataframe: pd.DataFrame):
    max_spread = Decimal("0")

    for row in book_record_dataframe.itertuples():
        asks = OrderBookEntry.from_list_many(row.asks)
        bids = OrderBookEntry.from_list_many(row.bids)

        highest_bid = max(obj.__getattribute__("price") for obj in bids)
        lowest_ask = min(obj.__getattribute__("price") for obj in asks)

        spread = highest_bid - lowest_ask
        if spread > max_spread:
            max_spread = spread
        return f"Max Spread - {max_spread}"
