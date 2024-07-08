from datetime import datetime

import pandas as pd
from deepdiff import DeepDiff

import batch


def dt(hour, minute, second=0):
    return datetime(2023, 1, 1, hour, minute, second)


def test_prepare_data():
    data = [
        (None, None, dt(1, 1), dt(1, 10)),
        (1, 1, dt(1, 2), dt(1, 10)),
        (1, None, dt(1, 2, 0), dt(1, 2, 59)),
        (3, 4, dt(1, 2, 0), dt(2, 2, 1)),
    ]

    columns = [
        'PULocationID',
        'DOLocationID',
        'tpep_pickup_datetime',
        'tpep_dropoff_datetime',
    ]
    df = pd.DataFrame(data, columns=columns)
    categorical = ['PULocationID', 'DOLocationID']

    actual_df = batch.prepare_data(df, categorical)

    actual_df_list_dicts = actual_df.to_dict('records')

    expected_data = [
        ('-1', '-1', dt(1, 1), dt(1, 10), 9.0),
        ('1', '1', dt(1, 2), dt(1, 10), 8.0),
    ]
    expected_columns = [
        'PULocationID',
        'DOLocationID',
        'tpep_pickup_datetime',
        'tpep_dropoff_datetime',
        'duration',
    ]
    expected_df = pd.DataFrame(expected_data, columns=expected_columns)

    expected_df_list_dicts = expected_df.to_dict('records')

    assert actual_df_list_dicts == expected_df_list_dicts

    diff = DeepDiff(actual_df_list_dicts, expected_df_list_dicts)
    print(f'diff = {diff}')

    assert 'type_changes' not in diff
