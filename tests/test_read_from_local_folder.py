from cryptoinsighto.load_data.read_from_local_folder import read_from_local_folder
from pathlib import Path


def test_read_from_local_folder():
    book_records = read_from_local_folder(Path("mock_data"))
    assert len(book_records) > 2
