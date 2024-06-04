# Earth Index Embeddings

## Submission Details

- **Submitter (Affiliation):** [Ben Strong](https://github.com/bengmstrong) (Earth Genome), [Hutch (Tom) Ingold](https://github.com/tingold) (Earth Genome)
- **Data Provider (Legal Entity):** Earth Genome (501(c)(3) Nonprofit)
- **Homepage:** http://earthindex.ai/

## Overview
Earth Index is a platform for tile-level geospatial search and classification of satellite imagery. Earth Index works by “pre-indexing” the planet for search using earth observation foundation models.

## Use Cases
We've been using embeddings for human-in-the-loop tile-level search (approximate nearest neighbors) and classification (linear or other lightweight models). Some downstream applications include monitoring targets like:
- [Poultry CAFOs](https://medium.com/earthrisemedia/finding-5-billion-chickens-with-human-in-the-loop-ai-model-tuning-via-earth-index-1d3f5cc89aec)
- Artisinal gold mining
- Infrastucture development (roads, dams, etc.)
- Landfills and waste sites

## Data
- **URL:** [tbd, on source.coop]
- **Documentation:** [tbd]
- **Projection:** EPSG:4326
- **License:** CC-BY

## Samples
- [sample_metadata.json](./sample_metadata.json)
- [embeddings.parquet](./21MTN.parquet)

## Validation
- GeoParquet validation: `gpq validate embeddings.parquet`
- Emb sample metadata and parquet metadata validation: `python3 validate.py`

## Columns
| Field Name | Type | Description |
|------------| ---- | ----------- |
| geometry   | geometry |Geometry of tile used to generate embeddings |
| id         | string | Unique identifier for tile |
| embedding  | array<float> | The vector embedding |

## File structure
The files originate from MGRS 100km x 100km imagery tile, e.g. `21MNT`, which the parquet files inherit.
That being said, using a filename as metadata is an easy way to lose context so we make sure that all relevant 
metadata from the filename also gets embedding in the file itself.


## Metadata
The `embedding.parquet` file is also a valid  [Geoparquet file](https://github.com/opengeospatial/geoparquet/blob/main/format-specs/geoparquet.md), with the expected metadata stored under the `geo` key. 
Additionally we have added an `emb` key for the embeddings metadata - also in JSON format. 

The metadata adheres to the [json schema](./schema.json) provided. For interoperability with STAC this schema references
some STAC schema elements, specifically [provider](https://schemas.stacspec.org/v1.0.0/item-spec/json-schema/provider.json), 
      [datetime](https://schemas.stacspec.org/v1.0.0/item-spec/json-schema/datetime.json)
and [licensing](https://schemas.stacspec.org/v1.0.0/item-spec/json-schema/licensing.json) 

### EMB Metadata

| Field Name      | Type                   | Description                                                           |
|-----------------|------------------------|-----------------------------------------------------------------------|
| version         | string                 | fixed at `0.0.1`  (required)                                          |
| model           | object<string, object> | see Model metadata                                                    |
| providers       | object<string, object> | provider metadata -- see [provider](https://schemas.stacspec.org/v1.0.0/item-spec/json-schema/provider.json) | 
| licensing       | object<string, object> | licensing metadata -- see [licensing](https://schemas.stacspec.org/v1.0.0/item-spec/json-schema/licensing.json)  |   
| datetime        | object<string, object> | datetime metadata -- see [datetime](https://schemas.stacspec.org/v1.0.0/item-spec/json-schema/datetime.json) |
| source_datasets | object<string, object> | datasets used to generate embeddings - see Dataset metadata |
| embedding       | object<string, object> | Embeddings metadata                                                   |



### Model metadata
| Field Name  | Type | Description                         |
|-------------| ---- |-------------------------------------|
| id          | string | id of model (required)              |
| source      | string | URI for model  (required)           |
| version     | string | version of model                    |
| family      | string | model family                        |
| name        | string | Name of model                       |
| description | string | human readable description of model |
| config      | string | Configuration of model; includes information needed to generate embeddings (e.g. what layers were extracted) |

### Dataset metadata
| Field Name  | Type | Description                                                      |
|-------------| ---- |------------------------------------------------------------------|
| id          | string | Dataset id (required)                                            |
| name        | string | Dataset used to generate the embeddings                          | 
| description | string | Dataset used to generate the embeddings                          | 
| source      | string | URI for dataset that was used by the embeddings model (required) |

### Embeddings metadata
| Field Name | Type | Description |
| ---------- | ---- | ----------- |
| dim | int | Embeddings size |
| quantization | string | Description of quantization scheme, if any |

## Design thoughts / open questions
- We also duplicate most of this metadata in STAC and have reused STAC metadata definitions to ease interoperability between parquet and STAC .
- We've opted to put the metadata within the `emb` key, in the same style as geoparquet. But we're not committed to this and are interested in other opinions.


