import os
from pathlib import Path
from datetime import datetime
import json
import time
from cryptoinsighto.types.book_record_storage import BookRecordStorage
import asyncio
from cryptoinsighto.coinbase_mock.get_order_book import get_order_book


def save_to_json(data: BookRecordStorage, request_time, output_dir):
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Generate filename with timestamp
    timestamp = request_time.strftime("%Y%m%d_%H%M%S")
    filename = f"coinbase_mock_bookrecord_{timestamp}.json"
    filepath = os.path.join(output_dir, filename)

    # Save data to JSON file
    with open(filepath, "w") as f:
        json.dump(data.model_dump_json(), f, indent=2)

    return filepath


def main():
    # Configuration
    OUTPUT_DIR = "mock_data"
    SYMBOL = "BTC-USD"
    DELAY_SECONDS = 5

    print(f"Starting mock data generator...")
    print(f"Saving files to: {os.path.abspath(OUTPUT_DIR)}")
    print(f"Generating records {DELAY_SECONDS} seconds")

    try:
        while True:
            # Generate batch of records
            book_order_dict = asyncio.run(get_order_book("BTC-USD"))
            request_timestamp = datetime.now()
            book_order_storage = BookRecordStorage(
                source="mock_coinbase", request_timestamp=request_timestamp, **book_order_dict
            )
            # Save to file
            filepath = save_to_json(book_order_storage, request_timestamp, OUTPUT_DIR)
            print(f"Saved book order records to {book_order_storage}")

            # Wait before next batch
            time.sleep(DELAY_SECONDS)

    except KeyboardInterrupt:
        print("\nStopping mock data generator...")


if __name__ == "__main__":
    main()
