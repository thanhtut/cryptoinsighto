from glob import glob
import json
from cryptoinsighto.types.book_record_storage import BookRecordStorage
import pandas as pd
from pydantic import ValidationError
from pathlib import Path


def read_from_local_folder(data_folder: Path):
    valid_records = []

    for file_path in data_folder.glob("*.json"):
        with open(file_path, "r") as f:
            try:
                data = json.load(f)
                data_dict = json.loads(data)
                validated_data = BookRecordStorage(**data_dict).model_dump()
                valid_records.append(validated_data)
            except json.JSONDecodeError as e:
                print(f"JSON decode error. Log and report. {file_path.name}: {str(e)}")

            except ValidationError as e:
                print(f"There is a validation error. Log and report. {file_path.name}: {str(e)}")
    # data validation is done here to ensure that only valid records gets to the dataframe
    validated_df = pd.DataFrame(valid_records) if valid_records else pd.DataFrame()
    validated_df = validated_df.sort_values("request_timestamp", ascending=True)
    return validated_df
