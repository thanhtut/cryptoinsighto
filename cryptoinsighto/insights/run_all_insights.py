import asyncio
from .analysis.forecast_linear_regression import run_analysis as run_analysis_forecast
from .analysis.max_spread import run_analysis as run_analysis_max_spread
from .analysis.highest_bid_lowest_ask import run_analysis as run_analysis_hbid_lask


async def run_all_insights(book_record_dataframe):
    tasks = [
        run_analysis_forecast(book_record_dataframe),
        run_analysis_max_spread(book_record_dataframe),
        run_analysis_hbid_lask(book_record_dataframe),
    ]

    results = await asyncio.gather(*tasks)
    return results
