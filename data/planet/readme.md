# Planet Embeddings

## Submission Details
- **Submitter (Affiliation):** Ash Hoover, Applied Machine Learning Engineer at Planet
- **Data Provider (Legal Entity):** Planet Labs, PBC
- **Homepage:** [https://www.planet.com/](https://www.planet.com/)

## Overview
Some samples of embeddings are included for demonstration purposes but are not fully representative of all of Planet's uses and approaches.

The three core fields organizing our embeddings are:
- **datetime:** when
- **geometry:** where (geospatial footprint)
- **embedding:** what (semantic vector)

Spatiotemporal indexing enables cross-referencing with other data sources and tools. Depending on the project or problem, we may organize our geoparquet files differently. For example, for a dense timeseries problem, we may use per-location geoparquet files with deep timestacks of embeddings (e.g., multiple years of daily data). For a broad area search problem, we may prefer embeddings from many locations in one file with separate files per thin time period. Ease of integration with visualization tools and ingestion into vector databases are also considerations.

The geometry field represents the footprint of the input imagery window from which an encoder model produced an embedding. A single datetime is useful when making embeddings from specifically timestamped individual images. However, there are scenarios where a datetime range is more appropriate. If embeddings or their corresponding input raster(s) represent timespans rather than points in time, then we would use `start_datetime` and `end_datetime` in place of the singular `datetime`.

Data quality fields such as `cloud_percent` are helpful augmentations when working with daily Planet embeddings. References to specific input assets, e.g., Planet `item_id` and `item_type`, can also be helpful for provenance tracking. We often have reference IDs to internal assets and services.

## Use Cases
Embeddings are used for multiple purposes at Planet, including:
- Search
- Featurization
- Classification
- Change Detection
- Downstream Tasks (e.g., derivative data production)

See some of our prior work with the [RapidAI4EO](https://rapidai4eo.eu/) effort as an example.

## Data
- **URL:** No public data yet
- **Documentation:** No public documentation yet
- **Projection:** EPSG:4326

### Samples
- [sample_embeddings_metadata.json](./sample_embeddings_metadata.json)
- [sample_embeddings.parquet](./sample_embeddings.parquet)

## Columns
| Field Name | Type | Description |
| ---------- | ---- | ----------- |
| geometry | geometry | Spatial footprint of an imagery chip fed into an encoder |
| datetime | datetime | Time of upstream imagery acquisition |
| embedding | float[] | Embedding (length is model-dependent) |
| embedding_thumbnail_uri | uri | Visual preview image of the embedded chip |
| cloud_percent | int | Percent of the input chip that is covered by clouds |
| clear_percent | int | Percent of the input chip that is clear |

## File Structure
File organization depends on the task. For a 5-year daily timeseries analysis, we would have separate files for each chip window with ~1825 rows (one row per day). Total filesize depends on auxiliary metadata and embedding size, but we end up in a ballpark of 3MB per embedding parquet file. Chip window size depends on the encoder model. Many models use sizes such as 224x224 or 256x256 pixels.

Naming convention is variable, but here is an example structured name pattern:
- `{project_ref}_{compute_job_ref}_{input_data_source_ref}_chip_size_224_{model_ref}_embeddings_{internal_id}_aoi__lat_-10_1814__lon_-48_3244__pixels_0_0_224_224.parquet`

This approach relies on structured file names to keep track of metadata.

## Metadata
Not using geoparquet footers for now, but we do include some metadata in the filename.

### File Metadata
| Field Name | Type | Description |
| ---------- | ----- | ---------- |
| project_ref | string | Internal identifier about an overall project or effort |
| compute_job_ref | string | Internal identifier about a specific process generating embeddings |
| input_data_source_ref | string | Internal identifier about imagery asset(s) used to make embeddings |
| chip_size | int | Input chip size describing the patch window from which each embedding is made |
| internal_id | int | Reference internal datasets |
| centroid_lat | float | Latitude of the input chip's centroid |
| centroid_lon | float | Longitude of the input chip's centroid |
| xmin | int | Pixel bounds in upstream image to reference chip window |
| xmax | int | Pixel bounds in upstream image to reference chip window |
| ymin | int | Pixel bounds in upstream image to reference chip window |
| ymax | int | Pixel bounds in upstream image to reference chip window |

## Design Thoughts / Open Questions
- Are embeddings consumed directly from parquet files for further analysis?
- Are embeddings ingested into vector and/or relational databases?
- Can we enable combined embedding similarity and spatial and temporal search?
- Can we index imagery on pre-existing grids, e.g., using the Web Mercator Grid for Planet Basemaps?
- What would it look like to have an "embeddings tileserver" where we have tileserver-like URLs that serve embeddings? Example: `https://example.com/embeddings/planet-basemaps/{mosaic_name}/{z}/{x}/{y}`

### Suggested Future Survey Additions:
1. **Data Quality Metrics:** Are there any quality metrics beyond data usability stats like `cloud_percent` or any other relevant factors that affect the quality of the embeddings.
2. **Tools Integration:** Provide more details on how embeddings can be integrated with popular data science and visualization tools and the benefits of such integrations. What are your preferred tools for working with embeddings?
3. **Performance Metrics:** When posisble, include more info on performance metrics or benchmarks used to evaluate embeddings. Data used for evaluation could guide additional metadata tracking.