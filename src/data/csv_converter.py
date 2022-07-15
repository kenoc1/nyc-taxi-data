import pandas as pd
import os

def convert_parquet_to_csv():
    for filename in os.listdir('../../data/raw/parquet/'):
        if filename.endswith(".parquet"):
            print(filename)
            parquet_file = os.path.join(filename[:-8]) + '.parquet'
            df = pd.read_parquet('../../data/raw/parquet/' + os.path.join(filename))
            df.to_csv('../../data/raw/csv/' + filename[:-8] + '.csv', index=False)