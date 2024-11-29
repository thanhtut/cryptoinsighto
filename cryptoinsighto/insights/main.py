import os
from cryptoinsighto.load_data.read_from_local_folder import read_from_local_folder
from .run_all_insights import run_all_insights
from pathlib import Path
import asyncio

DATA_SOURCE = os.getenv("DATA_SOURCE", "LOCAL")
LOCAL_DATA_FOLDER = os.getenv("LOCAL_DATA_FOLDER", "mock_data")


def main():
    # simulate loading of the data
    if DATA_SOURCE == "LOCAL":
        # this step should be replaced with actual data loading
        book_record_dataframe = read_from_local_folder(Path(LOCAL_DATA_FOLDER))
        # running them all should be done through
        # a message queue system
        # like rabbitmq or kefka
        asyncio.run(run_all_insights(book_record_dataframe))
    else:
        raise NotImplementedError()


if __name__ == "__main__":
    main()
