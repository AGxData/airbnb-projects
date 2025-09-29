import pandas as pd
from datetime import datetime
import os

inside_airbnb_urls = [
    "https://data.insideairbnb.com/united-states/ny/new-york-city/2025-08-01/data/listings.csv.gz",
    "https://data.insideairbnb.com/united-states/ny/new-york-city/2025-07-01/data/listings.csv.gz",
    "https://data.insideairbnb.com/united-states/ny/new-york-city/2025-06-17/data/listings.csv.gz",
    "https://data.insideairbnb.com/united-states/ny/new-york-city/2025-05-01/data/listings.csv.gz",
    "https://data.insideairbnb.com/united-states/ny/new-york-city/2025-04-01/data/listings.csv.gz",
    "https://data.insideairbnb.com/united-states/ny/new-york-city/2025-03-01/data/listings.csv.gz",
    "https://data.insideairbnb.com/united-states/ny/new-york-city/2025-02-01/data/listings.csv.gz",
    "https://data.insideairbnb.com/united-states/ny/new-york-city/2025-01-03/data/listings.csv.gz",
    "https://data.insideairbnb.com/united-states/ny/new-york-city/2024-12-04/data/listings.csv.gz",
    "https://data.insideairbnb.com/united-states/ny/new-york-city/2024-11-04/data/listings.csv.gz",
    "https://data.insideairbnb.com/united-states/ny/new-york-city/2024-10-04/data/listings.csv.gz"
]

data_folder = os.path.join("..", "data")
os.makedirs(data_folder, exist_ok = True)

for url in inside_airbnb_urls:
    date_str = url.split("/")[-3]
    date = datetime.strptime(date_str, "%Y-%m-%d")
    
    filename = f"{date.strftime("%b")}_{date.year}_listings.csv"
    path = os.path.join(data_folder, filename)
    
    df = pd.read_csv(url)
    df.to_csv(filename, index = False)