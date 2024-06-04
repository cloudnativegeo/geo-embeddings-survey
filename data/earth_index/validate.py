from jsonschema import validate
import json
import pyarrow.parquet as pq

instance = json.load(open('sample_metadata.json'))
schema = json.load(open('schema.json'))

schema = json.load(open('schema.json'))

print('Validating sample_metadata.json...')
try:
    validate(instance=instance,schema=schema)
    print('Validation successful!')
except Exception as e:
    print('Validation failed!')
    print(e)


print('Validating embeddings.parquet...')
try:
    parquet_file = pq.ParquetFile('embeddings.parquet')
    embedding_metadata = json.loads(parquet_file.metadata.metadata[b'emb'].decode('utf-8'))
    validate(instance=embedding_metadata, schema=schema)
    print('Validation successful!')
except Exception as e:
    print('Validation failed!')
    print(e)


