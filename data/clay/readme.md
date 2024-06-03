# Clay Embeddings

## Submission Details

- **Submitter (Affiliation):** Bruno Sánchez-Andrade Nuno, ED at Clay
- **Data Provider (Legal Entity):** Clay, a fiscally sponsored project of the [501(c)(3)](https://radiant.earth) Radiant Earth
- **Homepage:** [http://earthindex.ai/](https://madewithclay.org/)

## Overview
Clay, "AI for Earth," is a non-profit effort to bring the latest progress in AI and geospatial technology to most people and organizations. Clay uses open data, open source, open models, and responsible AI frameworks to make Earth observation a force for positive change. Clay creates, maintains, and releases the Clay model, which frontloads undifferenciated computation to enable faster, easier and cheaper use of geospatial data. We also create tools to integrate the model. Finally, we also create no-code apps to maximize usability and impact for non-technical users.

## Use Cases

## Data
- **URL:** [https://beta.source.coop/clay/clay-model-v0-embeddings/](https://beta.source.coop/clay/clay-model-v0-embeddings/)
- **Documentation:** [https://beta.source.coop/repositories/clay/clay-model-v0-embeddings/description/](https://beta.source.coop/repositories/clay/clay-model-v0-embeddings/description/)
- **Projection:** EPSG:6326 (WGS-84)
- **License:** [ODC-BY](https://opendatacommons.org/licenses/by/)

### Samples (optional)
- [03WVN_20220610_20220610_v001.gpq](03WVN_20220610_20220610_v001.gpq)
- [03WVN_20220610_20220610_v001_metadata.json](03WVN_20220610_20220610_v001_metadata.json)

## Columns
| Field Name | Type   | Description                                        |
|------------|--------|----------------------------------------------------|
| index      | int64  | Index of the subwindow within the MGRS tile.       |
| source_url | string | S3 URL where the source imagery lives as a TIFF    | 
| date       | date   | Date of embedding creation                         |
| embeddings | float[]| The embeddings                                     |
| geometry   | geometry | Geometry of the source location of the embedding |

## File Structure
Filename is `MGRS_date_range_version`

## Metadata
No additional metadata, just what's in the GeoParquet spec.

## Design Thoughts / Open Questions

This is a first draft releasing embeddings, done with Clay Model v0.1. These embeddings correspond to all the training input.

We already have a newer Clay Model v1 and are actively seeking feedback on what format and metadata to use.

Our current thinking is:

| Field Name                | Type     | Description                                                    | Rationale                                               |
|---------------------------|----------|----------------------------------------------------------------|---------------------------------------------------------|
| Universally Class Identifier | string  | Multi-Class-based identifier of the embedding: location, time, instrument, model, ...  | Allows to identify and parse class based on ID          |
| source_url                | string   | S3 URL where the source imagery lives as a COG TIFF            | Allows to pull a view of actual source when needed      |
| date                      | date     | Date of embedding creation                                     |                                                         |
| source_model              | string   | Model used to create the embedding                             |                                                         |
| loss                      | float    | Loss between the output using the embedding and the input      |                                                         |
| loss_metric               | string   | Metric used to measure difference between input and reconstruction |                                                         |
| source_creator            | string   | Originator                                                    | Allows to tag who, why created the embedding, e.g., an app |
| embeddings                | float[]  | The embedding                                                  |                                                         |
| geometry                  | geometry | Geometry of the source location of the embedding               |                                                         |

Since the v1 training is ~70x bigger, we are not planning to create all the embeddings until we QA their quality. Eventually, we plan to create embeddings for all the open data archives.

Specifically, we seek input on the value of adding a "loss" measure. Adding this should both inform the expected quality of the embedding representing the input image and help quickly identify unusual losses (e.g., clouds will probably yield very low losses, and unusual features will have high losses). We also don't know if we should allow different metrics.
