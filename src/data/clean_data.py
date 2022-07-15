import dask.dataframe as dd

import pandas as pd

import datetime

import time

import numpy as np


import os

import warnings


warnings.filterwarnings("ignore")

outliers_dataframe = pd.DataFrame(columns=['filename', 'number_of_records', 'outliers_trip_times',
                                           'outliers_trip_distance', 'outliers_speed',
                                           'outliers_fare', 'total_outliers', 'fraction_of_data_remaining'])


def remove_outliers(new_frame, file_name):
    number_of_records = new_frame.shape[0]
    print("Number of pickup records = ", number_of_records)

    temp_frame = new_frame[(new_frame['trip_times (min)'] >= 1) & (new_frame['trip_times (min)'] <= 720)]
    c = temp_frame.shape[0]
    print("Number of outliers from trip times analysis:", (number_of_records - c))
    outliers_trip_times = number_of_records - c

    temp_frame = new_frame[(new_frame["trip_distance"] > 0) & (new_frame["trip_distance"] < 26)]
    d = temp_frame.shape[0]
    print("Number of outliers from trip distance analysis:", (number_of_records - d))
    outliers_trip_distance = number_of_records - d

    temp_frame = new_frame[(new_frame['Speed (mph)'] > 0) & (new_frame['Speed (mph)'] <= 50)]
    e = temp_frame.shape[0]
    print("Number of outliers from speed analysis:", (number_of_records - e))
    outliers_speed = number_of_records - e

    temp_frame = new_frame[(new_frame['total_amount'] > 0) & (new_frame['total_amount'] <= 200)]
    f = temp_frame.shape[0]
    print("Number of outliers from fare analysis:", (number_of_records - f))
    outliers_fare = number_of_records - f

    new_frame = new_frame[(new_frame['trip_times (min)'] >= 1) & (new_frame['trip_times (min)'] <= 720)]
    new_frame = new_frame[(new_frame["trip_distance"] > 0) & (new_frame["trip_distance"] < 26)]
    new_frame = new_frame[(new_frame['Speed (mph)'] > 0) & (new_frame['Speed (mph)'] <= 50)]
    new_frame = new_frame[(new_frame['total_amount'] > 0) & (new_frame['total_amount'] <= 200)]

    total_outliers = number_of_records - new_frame.shape[0]
    fraction_of_data_remaining = round(float(new_frame.shape[0] / number_of_records), 4)
    print("Total outliers removed", total_outliers)
    global outliers_dataframe
    outliers_dataframe = outliers_dataframe.append(
        {'file_name': file_name, 'number_of_records': number_of_records, 'outliers_trip_times': outliers_trip_times,
         'outliers_trip_distance': outliers_trip_distance, 'outliers_speed': outliers_speed,
         'outliers_fare': outliers_fare,
         'total_outliers': total_outliers, 'fraction_of_data_remaining': fraction_of_data_remaining}, ignore_index=True)
    return new_frame


def convert_to_unix(s):
    return time.mktime(datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S').timetuple())


def return_with_trip_times(month):
    duration = month[['tpep_pickup_datetime', 'tpep_dropoff_datetime']].compute()
    # pickups and dropoffs to unix time
    duration_pickup = [time.mktime(datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S').timetuple()) for x in
                       duration['tpep_pickup_datetime'].values]
    duration_drop = [time.mktime(datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S').timetuple()) for x in
                     duration['tpep_dropoff_datetime'].values]
    # calculate duration of trips
    durations = (np.array(duration_drop) - np.array(duration_pickup)) / float(60)

    # append durations of trips and speed in miles/hr to a new dataframe
    new_frame = month.compute()

    new_frame['trip_times (min)'] = durations
    new_frame['pickup_times (unix)'] = duration_pickup
    new_frame['Speed (mph)'] = 60 * (new_frame['trip_distance'] / new_frame['trip_times (min)'])

    return new_frame


