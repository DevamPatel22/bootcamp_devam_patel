# Homework 05 - Data Storage

This homework practices saving and loading data in different formats. The goal is to keep raw data separate from processed data and use environment variables for file paths.

## Data Storage

This homework uses two data folders:

- `data/raw/` stores the original CSV version of the dataset.
- `data/processed/` stores the processed Parquet version of the dataset.

CSV is easy to inspect and share, while Parquet is useful because it preserves data types better and is efficient for larger datasets.

The notebook reads folder paths from a local `.env` file:

```text
DATA_DIR_RAW=data/raw
DATA_DIR_PROCESSED=data/processed