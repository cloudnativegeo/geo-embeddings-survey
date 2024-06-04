# Earth Index Embeddings

## Submission Details

- **Submitter (Affiliation):** Ben Strong (Earth Genome)
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
To be added soon

## Columns
| Field Name | Type | Description |
| ---------- | ---- | ----------- |
| geometry | geometry |Geometry of tile used to generate embeddings |
| tile_id | string | Unique identifier for tile |
| embedding | array<float> | The vector embedding |

## File structure
Within a set of embeddings, files are separated by MGRS 100km x 100km tile, e.g. `17SNB`. The tile name is also used for the name of the file.

This will likely change as we explore other grid systems.

## Metadata
Following the [Geoparquet Spec](https://github.com/opengeospatial/geoparquet/blob/main/format-specs/geoparquet.md), the following metadata is stored under the `geo` key in the Parquet metadata.

### File metadata

| Field Name | Type | Description |
| ---------- | ---- | ----------- |
| version | string | GeoParquet spec: version identifier |
| primary_column | string | GeoParquet spec: The name of the "primary" geometry column. |
| model | object<string, object> |Model metadata |
| dataset | object<string, object> | Dataset metadata |
| embedding | object<string, object> | Embeddings metadata |
| columns | object<string, Column Metadata> | GeoParquet spec: Metadata about geometry columns. Each key is the name of a geometry column in the table. |

### Model metadata
| Field Name | Type | Description |
| ---------- | ---- | ----------- |
| model_name | string | Name of model |
| model_source | string | URI for model |
| model_config | string |Configuration of model; includes information needed to generate embeddings (e.g. what layers were extracted) |

### Dataset metadata
| Field Name | Type | Description |
| ---------- | ---- | ----------- |
| dataset_name | string | Dataset used to generate the embeddings |
| dataset_date | string |  Date(s) that the dataset represents |
| dataset_source | string | URI for dataset that was used by the embeddings model |

### Embeddings metadata
| Field Name | Type | Description |
| ---------- | ---- | ----------- |
| embeddings_dim | int | Embeddings size |
| embeddings_quantization | string | Description of quantization scheme, if any |

## Design thoughts / open questions
- We also duplicate most of this metadata in STAC; a STAC extension for embeddings should also probably be part of this conversation.
- We've opted to put the metadata within the `geo` key, as this fundamentally builds on geoparquet. But we're not committed to this and are interested in other opinions.


