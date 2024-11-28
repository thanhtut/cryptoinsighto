from cryptoinsighto.coinbase_mock.get_order_book import get_order_book
from cryptoinsighto.types.book_record import BookRecord
from cryptoinsighto.types.order_book_entry import OrderBookEntry

import pytest


@pytest.mark.asyncio
async def test_get_order_book():
    book_dict = await get_order_book("BTC-USD")
    book_record = BookRecord(**book_dict)

    assert len(book_record.bids) > 0
    assert len(book_record.asks) > 0
    ask_entry = OrderBookEntry(
        price=book_record.asks[0][0], size=book_record.asks[0][1], num_orders=book_record.asks[0][2]
    )
    # testing data validation with pydantic models
    assert ask_entry.price > 0
    assert ask_entry.size > 0
    assert ask_entry.num_orders > 0
