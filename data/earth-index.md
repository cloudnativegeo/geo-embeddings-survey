# Earth Index Embeddings

## Submission Details

- **Submitter (Affiliation):** Ben Strong (Earth Genome)
- **Data Provider (Legal Entity):** Earth Genome (501(c)(3) Nonprofit)
- **Homepage:** http://earthindex.ai/

## Overview
Earth Index is a platform for tile-level geospatial search and classification of satellite imagery. Earth Index works by “pre-indexing” the planet for search using earth observation foundation models.

## Data
- **URL:** [tbd, on source.coop]
- **Documentation:** [tbd]
- **Projection:** EPSG:4326
- **License:** CC-BY

## Metadata
Following the [GeoparquetSpec](https://github.com/opengeospatial/geoparquet/blob/main/format-specs/geoparquet.md), the following metadata is stored under the `geo` key in the Parquet metadata.

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

## Columns
| Field Name | Type | Description |
| ---------- | ---- | ----------- |
| geometry | geometry |Geometry of tile used to generate embeddings |
| tile_id | string | Unique identifier for tile |
| embedding | array<float> | The vector embedding |












