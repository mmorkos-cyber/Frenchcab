import os
import pandas as pd



root = os.path.dirname(os.path.abspath(__file__))

dossier_data = os.path.join(root, "raw_data")

fichier_data_parquet = os.path.join(
    dossier_data,
    "yellow_tripdata_2026-01.parquet"
)

parquet_df = pd.read_parquet(fichier_data_parquet)

print("\n===== HEAD =====")
print(parquet_df.head())

print("\n===== SHAPE =====")
print(parquet_df.shape)

print("\n===== INFO =====")
parquet_df.info()

print("\n===== DESCRIPTION =====")
print(parquet_df.describe())

print("\n===== VALEURS NULLES =====")
print(parquet_df.isna().sum())

print("\n===== DOUBLONS =====")
print(parquet_df.duplicated().sum())

print("\n===== CONTROLES =====")
print("Negative prices:", (parquet_df["fare_amount"] < 0).sum())
print("Zero distance:", (parquet_df["trip_distance"] == 0).sum())
print("Zero passengers:", (parquet_df["passenger_count"] == 0).sum())



def transform(parquet_df):

    df = parquet_df.copy()

    print("\n===== TRANSFORM =====")
    print("Lignes avant :", len(df))

    df = df.drop_duplicates()
 
    df = df[df["fare_amount"] >= 0]

    df = df[df["trip_distance"] > 0]
  
    df = df[
        df["tpep_dropoff_datetime"]
        > df["tpep_pickup_datetime"]
    ]
  
    df["trip_duration_min"] = (
        df["tpep_dropoff_datetime"]
        - df["tpep_pickup_datetime"]
    ).dt.total_seconds() / 60

    df = df.reset_index(drop=True)

    print("Lignes après :", len(df))

    return df
