# ##################################
# Polars: CH7
# ##################################

import polars as pl

# Read DF
fruit_df = pl.read_csv("/Users/markroberts/tmp/python-polars-the-definitive-guide/data/fruit.csv")
print(fruit_df.head(15))

# Select columns:
print(fruit_df.select(pl.col("name"), "is_round", pl.col("^.*or.*$")))

# Filter on columnvalues:
print(fruit_df.filter((pl.col("weight") > 200) & (pl.col("is_round"))))

# Add columns:
print(fruit_df.with_columns(is_berry=pl.col("name").str.ends_with("berry")))

print("==========================")

# Aggregation
print(
    fruit_df.group_by(pl.col("origin").str.split(" ").list.last())
        .agg(
            pl.len().alias("occurrences"),
            average_wt = pl.col("weight").mean()
        )

)

# Sorting Rows:
print(
    fruit_df.sort(
        [pl.col("name").str.len_bytes(), pl.col("name")],
        descending=[True, False]
    )
)