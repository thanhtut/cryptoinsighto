import os
from cryptoinsighto.load_data.read_from_local_folder import read_from_local_folder

DATA_SOURCE = os.getenv("DATA_SOURCE", "LOCAL")
LOCAL_DATA_FOLDER = os.getenv("LOCAL_DATA_FOLDER", "mock_data")


def main():
    # simulate loading of the data
    if DATA_SOURCE == "LOCAL":
        book_record_dataframe = read_from_local_folder(LOCAL_DATA_FOLDER)

    else:
        raise NotImplementedError()


if __name__ == "__main__":
    main()
