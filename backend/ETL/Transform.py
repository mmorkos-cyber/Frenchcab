from Extract import parquet_df, pd

try:
    df = parquet_df.copy()
    doublons = df.duplicated().sum()
    #print(doublons)
    df = df.drop_duplicates()

    df = df[df["fare_amount"] >= 0]
    df = df[df["trip_distance"] > 0]

    df = df[df["tpep_dropoff_datetime"] > df["tpep_pickup_datetime"]]

    df["trip_duration_min"] = (df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"]).dt.total_seconds() / 60

    df = df.reset_index(drop=True)

    #print("Lignes après :", len(df))
    #colonne avec valeur NAN
    na_cols = ["passenger_count", "RatecodeID", "store_and_fwd_flag", "congestion_surcharge", "Airport_fee"]

    #valeur de défaut
    fill_values = {"passenger_count": 0, "RatecodeID": 99, "store_and_fwd_flag": "N", "congestion_surcharge": 0.0, "Airport_fee": 0.0}
    mask = df[na_cols].isna().sum(axis=1) >= 2
    df.loc[mask, na_cols] = df.loc[mask, na_cols].fillna(value=fill_values)

    """print("Rows filled:", mask.sum())

    print(df[na_cols].isna().sum())
    print(df.isna().sum())"""

    print(df.info())
    #print(df.describe())
    #print(df.head())
    print("File transformed:", df.shape)
except FileNotFoundError:
    print("File not found:", parquet_df)
except Exception as e:
    print("Error while reading the file:", e)

