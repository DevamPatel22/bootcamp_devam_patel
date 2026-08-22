# Homework 06 - Data Preprocessing

This homework applies basic preprocessing steps to a raw dataset and saves a cleaned version for later analysis.

## Cleaning Strategy

The preprocessing notebook uses reusable functions from `src/cleaning.py`.

The cleaning steps are:

- fill missing numeric values with the median
- drop rows with missing values in selected columns when needed
- normalize numeric columns with min-max scaling

The raw dataset is stored in `data/raw/`, and the cleaned output is saved in `data/processed/`.

## Assumptions

- Median filling is used for numeric columns because it is less affected by extreme values than the mean.
- Min-max normalization is used to scale numeric columns to a common range.
- The sample dataset is small, so the cleaning process is mainly used to demonstrate the workflow.