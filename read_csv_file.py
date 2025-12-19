import pandas as pd

# The direct link to the data file is this:
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"


# Read the CSV file into a DataFrame from URL
df_url = pd.read_csv(url, header=None)


# Read the CSV file into a DataFrame from .csv file
df_local = pd.read_csv("data/01_automobile_dataset.csv", header=None)

# Display the first 5 rows of both DataFrames without headers
print("From URL (without headers):")
print(df_url.head(5))

print("\nFrom Local File (without headers):")
print(df_local.head(5))


# Define the headers
headers = [
    "symboling",
    "normalized-losses",
    "make",
    "fuel-type",
    "aspiration",
    "num-of-doors",
    "body-style",
    "drive-wheels",
    "engine-location",
    "wheel-base",
    "length",
    "width",
    "height",
    "curb-weight",
    "engine-type",
    "num-of-cylinders",
    "engine-size",
    "fuel-system",
    "bore",
    "stroke",
    "compression-ratio",
    "horsepower",
    "peak-rpm",
    "city-mpg",
    "highway-mpg",
    "price",
]

df_url.columns = headers

df_local.columns = headers
# Display the first 5 and last 5 rows of both DataFrames with headers
print("From URL (with headers):")
print(df_url.head(5))

print("\nFrom Local File (with headers):")
print(df_local.head(5))

# Save the DataFrame with headers to a new CSV file
df_local.to_csv(
    "data/02_automobile_dataset_with_header.csv",
    index=False,
)
