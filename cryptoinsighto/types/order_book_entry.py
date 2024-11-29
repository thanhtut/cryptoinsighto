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

    # DO NOT CHANGE THIS FIELD ORDER
    price: Decimal = Field()
    size: Decimal = Field()
    num_orders: int = Field(default=1)

    @field_validator("price", "size")
    def validate_positive(cls, v):
        """Ensure price and size are positive"""
        if v <= 0:
            raise ValueError("Price and size must be positive")
        return v

    @classmethod
    def from_list(cls, values: List) -> "OrderBookEntry":
        """Initialize from [price, size, num_order]."""
        fields = list(cls.model_fields.keys())

        # Validate that we have the correct number of values
        if len(values) != len(fields):
            raise ValueError(
                f"Expected {len(fields)} values but got {len(values)}. "
                f"Required fields: {', '.join(fields)}"
            )

        field_dict = dict(zip(fields, values))
        return cls(**field_dict)

    @classmethod
    def from_list_many(cls, list_of_values: List[List]) -> List["OrderBookEntry"]:
        """Create from list of asks and bids."""
        return [cls.from_list(values) for values in list_of_values]
