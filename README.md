# geo-embeddings-survey
A survey of use cases and current data schemas for vector embeddings in [GeoParquet](https://geoparquet.org/)

## About

This repository serves as a survey of all attempts to store geospatial embeddings in GeoParquet. This generally seems like a good idea, and it'd be good for everyone if there was a consistent approach for how to do this. The hope with this repo is to gather all the information of what people have done, along with any additional ideas, and then work to make a lightweight specification / set of recommendations for how to store embeddings in GeoParquet. 

After we have sufficient submissions here we'll find a time to gather a group to draft an attempt at those recommendations. 

## Submitting

Contributions are very welcome. If you've created geospatial embeddings just make a copy of the [template](template.md), update it with your information, and put it in a folder named after your organization. And then ideally also put in a small sample geoparquet file. And do please run [scripts/parquet_metadata_to_json.py](scripts/parquet_metadata_to_json.py) to make a more human readable copy of the json metadata in your geoparquet file. It is ok if you didn't customize the parquet metadata at all, it's still valuable to just see how the geoparquet spec is being used. 
