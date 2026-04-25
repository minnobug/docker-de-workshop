import sys
import pandas as pd

month = int(sys.argv[1])

print("arguments", sys.argv)

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})

print(df.head())

df.to_parquet(f"output_month_{sys.argv[1]}.parquet")

print(f"Running pipeline for month {month}")