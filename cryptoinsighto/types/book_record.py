from typing import List, Union
from pydantic import BaseModel, Field, field_validator
from decimal import Decimal
from .order_book_entry import OrderBookEntry


class BookRecord(BaseModel):
    """
    Coinbase Level 2 order book response
    """

    bids: List[List[Union[str, Decimal]]] = Field(..., description="List of bid orders")
    asks: List[List[Union[str, Decimal]]] = Field(..., description="List of ask orders")
    sequence: int = Field(..., description="Sequence number of the order book")

    @field_validator("bids", "asks")
    @classmethod
    def validate_order_book_entry(cls, v):
        if len(v) < 2:
            raise ValueError("Order book entry must have at least price and size")

        # Add num_orders if not present
        if len(v) < 3:
            v.append(1)

        return v
