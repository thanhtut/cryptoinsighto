import pandas as pd
from .run_analysis_wrapper import run_analysis
from typing import List
from cryptoinsighto.types.book_record_storage import BookRecordStorage
from cryptoinsighto.types.order_book_entry import OrderBookEntry
from sklearn.linear_model import LinearRegression
import numpy as np

ANALYSIS_NAME = "forecast_linear_regression"


@run_analysis(ANALYSIS_NAME)
def run_analysis(book_record_dataframe: List[BookRecordStorage]):
    # mid price is average of bid and ask
    historical_mid_prices = []
    for row in book_record_dataframe.itertuples():
        asks = OrderBookEntry.from_list_many(row.asks)
        bids = OrderBookEntry.from_list_many(row.bids)

        highest_bid = max(obj.__getattribute__("price") for obj in bids)
        lowest_ask = min(obj.__getattribute__("price") for obj in asks)
        historical_mid_prices.append((highest_bid + lowest_ask) / 2)

    y = np.array(historical_mid_prices)
    X = np.arange(len(historical_mid_prices)).reshape(-1, 1)

    # Fit the model
    model = LinearRegression()
    model.fit(X, y)

    future_X = np.arange(len(historical_mid_prices), len(historical_mid_prices) + 1).reshape(-1, 1)

    future_predictions = model.predict(future_X)

    return f"The future price is {future_predictions.tolist()}"
