from typing import List, Union
from decimal import Decimal
from pydantic import BaseModel, Field, field_validator, ConfigDict


def decimal_encoder(d: Decimal) -> str:
    return str(d)


class OrderBookEntry(BaseModel):
    """
    Represents a single order book entry (bid or ask)
    """

    model_config = ConfigDict(
        json_encoders={
            # Specify how to encode Decimal types
            Decimal: decimal_encoder
        }  # TODO: this is deprecated removed in Pydantic v3.
    )

    price: Decimal = Field()
    size: Decimal = Field()
    num_orders: int = Field(default=1)

    @field_validator("price", "size")
    def validate_positive(cls, v):
        """Ensure price and size are positive"""
        if v <= 0:
            raise ValueError("Price and size must be positive")
        return v
