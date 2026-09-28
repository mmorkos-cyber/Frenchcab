import os 
import pandas as pd
import sqlite3

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
dossier_data = os.path.join(root, "raw_data")

fichier_data_parquet = os.path.join(dossier_data, "yellow_tripdata_2026-01.parquet")

parquet_df = pd.read_parquet(fichier_data_parquet)