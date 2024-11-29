from .book_record import BookRecord
from pydantic import Field, ConfigDict
from datetime import datetime


class BookRecordStorage(BookRecord):
    """
    Internal book record storage.
    The porpose of this is to support multiple book record sources in the future
    """

    # should be an enum
    source: str = Field(..., description="Sequence number of the order book")
    # response time
    request_timestamp: datetime = Field(..., description="Time that the request was sent")

    # TODO: probably need to add market symbol here too

    model_config = ConfigDict(
        use_tz=True  # timezone awareness
    )
