# Adapted from https://github.com/opengeospatial/geoparquet/blob/main/scripts/update_example_schemas.py
# to translate any input parquet file's metadata to json. It creates a json file of the same name
# as the input file, suffixed with _metadata.json.

import json
from pathlib import Path
from typing import Dict, Union, Any
import pyarrow.parquet as pq

def copy_parquet_schema_metadata_to_json(parquet_file: Path) -> None:
    """Copy Parquet schema metadata to a neighboring JSON file"""
    neighboring_json_file = parquet_file.with_name(f"{parquet_file.stem}_metadata.json")
    schema = pq.read_schema(parquet_file)
    decoded_meta = decode_dict(schema.metadata)

    with open(neighboring_json_file, "w") as f:
        json.dump(decoded_meta, f, indent=2, sort_keys=True)


def decode_dict(d: Dict[Union[bytes, str], Union[bytes, Any]]) -> Dict[str, Any]:
    """Decode binary keys and values to string and dict objects"""
    new_dict = {}
    for key, val in d.items():
        new_key = key.decode() if isinstance(key, bytes) else key
        new_val = val.decode() if isinstance(val, bytes) else val
        if isinstance(new_val, str) and new_val.lstrip().startswith("{"):
            new_val = json.loads(new_val)

        new_dict[new_key] = new_val

    return new_dict


def main(parquet_file_name: str):
    parquet_file = Path(parquet_file_name)
    copy_parquet_schema_metadata_to_json(parquet_file)


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python parquet_metadata_to_script.py <parquet_file>")
    else:
        main(sys.argv[1])
