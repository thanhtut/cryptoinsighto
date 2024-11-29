import pandas as pd
from .run_analysis_wrapper import run_analysis
from typing import List
from cryptoinsighto.types.order_book_entry import OrderBookEntry
from datetime import timedelta

ANALYSIS_NAME = "highest_bid_lowest_ask"


@run_analysis(ANALYSIS_NAME)
def run_analysis(book_records_dataframe: pd.DataFrame):
    """
    Compute highest bid and lowest asks at ever 5 seconds
    """
    time_delta = timedelta(seconds=100)
    previous_timestamp = None
    output = ""
    for row in book_records_dataframe.itertuples():
        if previous_timestamp is None or time_delta.total_seconds() > 4:
            if previous_timestamp is not None:
                time_delta = row.request_timestamp - previous_timestamp
            previous_timestamp = row.request_timestamp

            # compute highest bid and lowest ask
            asks = OrderBookEntry.from_list_many(row.asks)
            bids = OrderBookEntry.from_list_many(row.bids)

            highest_bid = max(obj.__getattribute__("price") for obj in bids)
            lowest_ask = min(obj.__getattribute__("price") for obj in asks)

            output = (
                output
                + "\n"
                + f"Highest bid is {highest_bid} and lowset asks is {lowest_ask} at {row.request_timestamp}"
            )
    return output
