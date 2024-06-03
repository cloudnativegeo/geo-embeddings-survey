# Survey for current practices storing embeddings in GeoParquet

A repository that serves as survey of use cases and current data schemas for vector embeddings in [GeoParquet](https://geoparquet.org/).

## About

This repository serves as a survey of all attempts to store geospatial embeddings in GeoParquet. This generally seems like a good idea, and it'd be good for everyone if there was a consistent approach for how to do this. The hope with this repo is to gather all the information of what people have done, along with any additional ideas, and then work to make a lightweight specification / set of recommendations for how to store embeddings in GeoParquet (or other geospatial formats.

After we have sufficient submissions here we'll find a time to gather a group to draft an attempt at those recommendations. 

## Submitting

Contributions are very welcome. If you've created geospatial embeddings just clone the repo, make a copy of the [template](template.md), update it with your information, and put it in a folder named after your organization. And then ideally also put in a small sample geoparquet file. And do please run [scripts/parquet_metadata_to_json.py](scripts/parquet_metadata_to_json.py) to make a more human readable copy of the json metadata in your geoparquet file. It is ok if you didn't customize the parquet metadata at all, it's still valuable to just see how the geoparquet spec is being used. 

To submit your information just create a pull request for the repo. You'll then be given commit rights, so you can continue to update after the initial PR. If you are not comfortable creating PR's then just file an [issue](https://github.com/cloudnativegeo/geo-embeddings-survey/issues) and someone can help you get it submitted.

And please note, the submissions do not need to be on 'open' embeddings datasets - we're just looking to standardize, so if you're working with proprietary data just fill out what you can. You are welcome to put up an example dataset with a proprietary license, or to just describe the dataset. Submissions that are storing geospatial embeddings but aren't using GeoParquet are also welcome - but do please adapt the metadata questions to the file format. 

## Current submissions

 * [Earth Index](data/earth_index)
 * [Clay](data/clay)
