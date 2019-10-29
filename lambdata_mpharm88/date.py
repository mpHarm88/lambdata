"""
This is a function for taking a date column and using pandas to transform it into 5 new columns:
    pandas date time column including day, month, and year
    dedicated day column 
    dedicated month column 
    dedicated year column
    dedicated season column - {3,4,5:spring, 6,7,8:summer, 9,10,11:autumn, 12,1,2:winter}
"""

import pandas as pd


def date(df, col):
    """
    This is a function for turning a date column that includes month, day, and year
    into 5 separate columns that includes: Pandas date time, year, month, day, season.
    Seasons identified as: {3,4,5:spring, 6,7,8:summer, 9,10,11:autumn, 12,1,2:winter} 
    """
    df = df.copy()
    season = {1: 'winter',
              2: 'winter',
              3: 'spring',
              4: 'spring',
              5: 'spring',
              6: 'summer',
              7: 'summer',
              8:  'summer',
              9: 'autumn',
              10: 'autumn',
              11: 'autumn',
              12: 'winter'}
    df = pd.DataFrame(data=df)
    df['pd_date_time'] = pd.to_datetime(df[col])
    df['day'] = df['pd_date_time'].dt.day
    df['month'] = df['pd_date_time'].dt.month
    df['year'] = df['pd_date_time'].dt.year
    df['season'] = df['month'].map(season)
    return df
