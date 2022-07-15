import pandas as pd
import os


def randomize_data():
    path = '../../data/interim/cleaned_csv/'
    path_to = '../../data/interim/cleaned_csv/'
    for filename in os.listdir(path):
        if filename.endswith(".csv"):
            print(filename)
            df_month_data = pd.read_csv(path + os.path.join(filename), low_memory=False)
            print(df_month_data.columns)
            df_month_data = df_month_data.sample(frac=1)
            df_month_data = df_month_data.drop(['Unnamed: 0'], axis=1)
            df_month_data.to_csv(path_to + filename, index=False)


def aggregate_data_for_one_year(number_of_rows_in_one_month):
    global df_final
    path = '../../data/interim/cleaned_csv/'
    for index, filename in enumerate(os.listdir(path)):
        if filename.endswith(".csv"):
            if index == 0:
                df_final = pd.read_csv(path + os.path.join(filename), low_memory=False,
                                       nrows=number_of_rows_in_one_month)
            else:
                df_final = pd.concat([df_final, pd.read_csv(path + os.path.join(filename), low_memory=False,
                                                            nrows=number_of_rows_in_one_month)])
            print(filename)
    df_final.to_csv('../../data/processed/randomized_aggregated_for_one_year.csv', index=False)
    print('Ready')
