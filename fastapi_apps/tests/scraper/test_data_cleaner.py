from apps.scraper.hotel_data.data_cleaner.hotel_data_cleaner import clean_hotel_data
import pandas as pd


def test_cleaned_hotel_data(
    hotel_cleaned_df, hotel_uncleaned_df, modify_row_and_columns_for_consistent_ordering
):
    cleaned_hotel_data = clean_hotel_data(df=hotel_uncleaned_df)
    cleaned_hotel_data = modify_row_and_columns_for_consistent_ordering(
        df=cleaned_hotel_data
    )
    pd.testing.assert_frame_equal(cleaned_hotel_data, hotel_cleaned_df)
