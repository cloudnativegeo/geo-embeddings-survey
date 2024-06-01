# Clay Embeddings

## Submission Details

- **Submitter (Affiliation):** Chris Holmes (Cloud Native Geo Foundation) - (switch to a real Clay contact when they take over)
- **Data Provider (Legal Entity):** Clay, a fiscally sponsored project of the (501(c)(3) [Radiant Earth](https://radiant.earth)
- **Homepage:** [http://earthindex.ai/](https://madewithclay.org/)

## Overview
TODO: Real overview by someone from Clay

## Data
- **URL:** https://beta.source.coop/clay/clay-model-v0-embeddings/
- **Documentation:** https://beta.source.coop/repositories/clay/clay-model-v0-embeddings/description/
- **Projection:** EPSG:6326 (WGS-84)
- **License:** [ODC-BY](https://opendatacommons.org/licenses/by/)

### Samples (optional)

* [03WVN_20220610_20220610_v001.gpq](03WVN_20220610_20220610_v001.gpq)
* [03WVN_20220610_20220610_v001_metadata.json](03WVN_20220610_20220610_v001_metadata.json]

## Columns
| Field Name | Type | Description |
| ---------- | ---- | ----------- |
| index      | int64 | ?          |
| source_url | string | s3 URL where the ? lives as a tif | 
| date       | date | date of ? |
| embeddings | float[] | the embeddings
| geometry | geometry | geometry of the tile |


## File structure

*filename is ? and the date?*

## Metadata
No additional metadata, just what's in the GeoParquet spec.

## Design thoughts / open questions

*Things considered in the design of this, and any open questions of things you'd went back and forth on / would like to know what others did*
 












