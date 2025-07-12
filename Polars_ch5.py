# ##################################
# Polars: CH5
# ##################################

import polars as pl
import time

start = time.time()
# Read taxi trips dataset.
trips = pl.read_parquet("/Users/markroberts/tmp/python-polars-the-definitive-guide/data/taxi/yellow_tripdata_*.parquet")

sum_per_vendor = trips.group_by("VendorID").sum()
income_per_distance_per_vendor = sum_per_vendor.select("VendorID",
                                                       income_per_distance = pl.col("total_amount")/pl.col("trip_distance"))
top_3 = income_per_distance_per_vendor.sort(by="income_per_distance", descending=True).head(3)
end = time.time()
print(top_3)
print(f"Duration: {(end - start):.3f}")