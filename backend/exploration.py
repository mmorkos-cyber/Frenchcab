import os 
import pandas as pd
import sqlite3

root = os.path.dirname(os.path.abspath(__file__))
dossier_data = os.path.join(root, "raw_data")

fichier_data_parquet = os.path.join(dossier_data, "yellow_tripdata_2026-01.parquet")

parquet_df = pd.read_parquet(fichier_data_parquet)

#print(parquet_df.head())
#print(parquet_df.info())
#print(parquet_df.describe())
#print(parquet_df.isna().sum())

#print("Negative prices:", (parquet_df["fare_amount"] < 0).sum())
#print("Zero distance:", (parquet_df["trip_distance"] == 0).sum())
print("Zero passengers:", (parquet_df["passenger_count"] == 0).sum())