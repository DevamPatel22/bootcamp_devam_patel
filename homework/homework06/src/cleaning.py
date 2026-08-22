import pandas as pd


def fill_missing_median(dataframe, columns):
    """Fill missing values in selected numeric columns with each column median."""
    cleaned = dataframe.copy()
    for column in columns:
        cleaned[column] = cleaned[column].fillna(cleaned[column].median())
    return cleaned


def drop_missing(dataframe, columns=None):
    """Drop rows with missing values in selected columns or the full DataFrame."""
    cleaned = dataframe.copy()
    return cleaned.dropna(subset=columns)


def normalize_data(dataframe, columns):
    """Normalize selected numeric columns using min-max scaling."""
    cleaned = dataframe.copy()
    for column in columns:
        min_value = cleaned[column].min()
        max_value = cleaned[column].max()

        if max_value == min_value:
            cleaned[column] = 0
        else:
            cleaned[column] = (cleaned[column] - min_value) / (max_value - min_value)

    return cleaned