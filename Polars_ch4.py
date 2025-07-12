# ##################################
# Polars: CH4
# ##################################

import polars as pl

# Series:
series_1 =pl.Series("sales", [150.0, 300.0, 250.0])
print(series_1)

# Dataframe - from Series:
df_1 = pl.DataFrame(
    {
        "col_1": series_1,
        "col_2": [24, 25, 26]
    }
)
print(df_1)

# Lazy loading:
# *** Needs graphviz with dot:
# *** brew install graphviz
#
df_lazy = pl.scan_csv("/Users/markroberts/tmp/python-polars-the-definitive-guide/data/fruit.csv") \
            .with_columns(is_heavy=pl.col("weight") > 200)

# Show the graph.
# df_lazy.show_graph()

# Nested Data types:
#   Polars has 3 nested data types: Array, List and Struct.
#   Array
coords = pl.DataFrame(
    [
        pl.Series("point_2d", [[1,3], [2,5], [4,6]]),
        pl.Series("point_3d", [[1,2,3], [9,8,7], [4,6,5]])
    ],
    schema = {
    "point_2d": pl.Array(shape=2, inner=pl.Int64),
    "point_3d": pl.Array(shape=3, inner=pl.Int64),
    }
)
print(coords)

print("=======")

# List:
weather = pl.DataFrame(
    {"temp": [[72.5, 75.0, 73.2], [68.0, 70.2]],
     "wind": [[15,20], [10,12,14,16]]
    }
)
print(weather)

print("=======")

# Sruct:
ratings_series = pl.Series(
    [
        {"movie": "Cars", "Theatre": "NE", "Avg_Rating": 4.5},
        {"movie": "Toy Story", "Theatre": "ME", "Avg_Rating":4.9}
    ]
)
print(ratings_series)

# Missing Values.
# ALL datatypes (incl. numeric) have missing values represented by null.
missing_df = pl.DataFrame(
    {
        "value": [None, 2, 3, 4, None, None, 7, 8, 9, None]
    }
)
print(missing_df)

# Can fill missing values in different ways:
print(missing_df.with_columns(filled_with_single=pl.col("value").fill_null(-1)))

# Or use a strategy:
new_df = missing_df.with_columns(
    forward = pl.col("value").fill_null(strategy="forward"),
    backward = pl.col("value").fill_null(strategy="backward"),
    min = pl.col("value").fill_null(strategy="min"),
    max = pl.col("value").fill_null(strategy="max"),
    mean = pl.col("value").fill_null(strategy="mean"),
    zero = pl.col("value").fill_null(strategy="zero"),
    one = pl.col("value").fill_null(strategy="one"),
)
print(new_df)

# Interpolate:
print(missing_df.interpolate())

# Data Type Conversion:
str_df = pl.DataFrame({"id": ["10000", "20000", "30000"]})
print(str_df)

int_df = str_df.select(pl.col("id").cast(pl.UInt16))
float_dr = str_df.select(pl.col("id").cast(pl.Float64))
print(int_df)
print(float_dr)