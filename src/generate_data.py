import os
import dask.dataframe as dd
from src.data.clean_data import remove_outliers, outliers_dataframe, return_with_trip_times
from src.data.csv_converter import convert_parquet_to_csv

# Da alle Dateien zur Verfügung zu stellen sehr viel Datenmenge benötigt dient das Skript dazu die Daten vollständig zu generieren
# Das folgende Skript benötigt alle Parquet Files des Jahres 2019 im Ordner: data/raw/parquet/
# Diese können auf der Internetseite gedownloadet werden
from src.data.preprocess_data_for_ml import randomize_data, aggregate_data_for_one_year

convert_parquet_to_csv()

for filename in os.listdir('../data/raw/csv/'):
    if filename.endswith(".csv"):
        print('Starting with the file:' + filename)
        dd_dataframe = dd.read_csv('../data/raw/csv/' + os.path.join(filename))
        pd_dataframe = return_with_trip_times(dd_dataframe)
        pd_dataframe = remove_outliers(pd_dataframe, filename)
        pd_dataframe.to_csv('../data/interim/cleaned_csv/' + filename[:-4] + '.csv')
        print('---------------------------------')

outliers_dataframe.to_csv('../reports/data_cleaning/outliers_result.csv')

randomize_data()
aggregate_data_for_one_year(500000)