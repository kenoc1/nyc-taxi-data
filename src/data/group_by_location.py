import csv

import pandas as pd
import os
import numpy as np


def group_by_location():
    # location number 0 for Pick-up and location_number 1 for Drop-off
    for filename in os.listdir('../../data/interim/cleaned_csv/'):
        if filename.endswith(".csv"):
            csv_file = os.path.join(filename[:-4]) + '.csv'
            print(csv_file)
            df = pd.read_csv('../../data/interim/cleaned_csv/' + os.path.join(filename), low_memory=False)

            df_group_by_pu_location = df.groupby('PULocationID').agg(pickup_count=('VendorID', 'size'),
                                                                     trip_distance_average=('trip_distance', 'mean'),
                                                                     minutes_average=(
                                                                         'trip_times (min)', 'mean'),
                                                                     total_amount_average=(
                                                                     'total_amount', 'mean')).reset_index()

            df_group_by_do_location = df.groupby('DOLocationID').agg(dropoff_count=('VendorID', 'size'),
                                                                     trip_distance_average=('trip_distance', 'mean'),
                                                                     minutes_average=(
                                                                         'trip_times (min)', 'mean'),
                                                                     total_amount_average=(
                                                                     'total_amount', 'mean')).reset_index()

            df_group_by_pu_location.to_csv('../../data/interim/grouped_by_location/pu_location/' + filename, index=False)
            df_group_by_do_location.to_csv('../../data/interim/grouped_by_location/do_location/' + filename, index=False)


def grouped_by_location_year():
    grouped_by_pu_location_year = pd.DataFrame()
    grouped_by_do_location_year = pd.DataFrame()
    for filename in os.listdir('../../data/interim/grouped_by_location/pu_location/'):
        if filename.endswith(".csv"):
            csv_file = os.path.join(filename[:-4]) + '.csv'
            print(csv_file)
            grouped_by_pu_location_year = pd.concat([grouped_by_pu_location_year, pd.read_csv(
                '../../data/interim/grouped_by_location/pu_location/' + os.path.join(filename), low_memory=False)])
    print(grouped_by_pu_location_year)
    df_group_by_pu_location = grouped_by_pu_location_year.groupby('PULocationID').agg(pickup_count=('pickup_count', 'size'),
                                                                                      trip_distance_average=(
                                                                                      'trip_distance_average', 'mean'),
                                                                                      minutes_average=(
                                                                                          'minutes_average', 'mean'),
                                                                                      total_amount_average=(
                                                                                      'total_amount_average',
                                                                                      'mean')).reset_index()

    for filename in os.listdir('../../data/interim/grouped_by_location/do_location/'):
        if filename.endswith(".csv"):
            csv_file = os.path.join(filename[:-4]) + '.csv'
            print(csv_file)
            grouped_by_do_location_year = pd.concat([grouped_by_do_location_year, pd.read_csv(
                '../../data/interim/grouped_by_location/do_location/' + os.path.join(filename), low_memory=False)])
    df_group_by_do_location = grouped_by_do_location_year.groupby('DOLocationID').agg(dropoff_count=('dropoff_count', 'size'),
                                                                                      trip_distance_average=(
                                                                                      'trip_distance_average', 'mean'),
                                                                                      minutes_average=(
                                                                                          'minutes_average', 'mean'),
                                                                                      total_amount_average=(
                                                                                      'total_amount_average',
                                                                                      'mean')).reset_index()

    df_group_by_pu_location.to_csv('../../data/interim/pu_location_aggregated.csv', index=False)
    df_group_by_do_location.to_csv('../../data/interim/do_location_aggregated.csv', index=False)



