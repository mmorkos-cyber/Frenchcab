from Extract import parquet_df

try:
    df = parquet_df.copy()

    print("\n===== TRANSFORM =====")
    print("Lignes avant :", len(df))
    df = df.drop_duplicates()

    df = df[df["fare_amount"] >= 0]
    df = df[df["trip_distance"] > 0]

    df = df[df["tpep_dropoff_datetime"] > df["tpep_pickup_datetime"]]

    df["trip_duration_min"] = (df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"]).dt.total_seconds() / 60

    df = df.reset_index(drop=True)

    print("Lignes après :", len(df))

    print(df)
    print(df.isna().sum())
    print("File transformed:", df.shape)
except FileNotFoundError:
    print("File not found:", parquet_df)
except Exception as e:
    print("Error while reading the file:", e)

