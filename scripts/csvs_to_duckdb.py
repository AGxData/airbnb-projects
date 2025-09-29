# Importing libraries for creating a single file to access all tables individually
import os
import duckdb as ddb


# Pointing towards the directory of this file
script_folder = os.path.dirname(os.path.abspath(__file__))

# Pointing towards the directory of the data file
data_folder = os.path.join(script_folder, "..", "data")
csvs = []

# Looping through CSV files in the data folder of the repo
for file in os.listdir(data_folder):
    if file.endswith(".csv"):
        path = os.path.join(data_folder, file)
        csvs.append(path)

# Placing file in the data folder
duckdb_file = os.path.join(data_folder, "airbnb_listings.duckdb")

# DuckDB connection
con = ddb.connect(duckdb_file)

# Looping through each CSV file to create a table out of each CSV and remove .csv file extension
for file in csvs:
    table_name = os.path.splitext(os.path.basename(file))[0]
    table_name = str(table_name).lower()
    file_path = file.replace("\\", "/") # Because Windows slashes...
    
    con.execute(f"""
    CREATE TABLE {table_name} AS 
    SELECT * 
    FROM read_csv_auto('{file_path}')
    """)


# table_names = []

# # Looping through each CSV files to get names
# for file in csvs:
#     name = os.path.splitext(os.path.basename(file))[0]
#     name = str(name).lower()
#     table_names.append(name)

# # Looping through each table and concatenating them into one single listings table to view all data at once
# if table_names:
#     union = ""
#     for i, table in enumerate(table_names):
#         if i == 0:
#             union += f"SELECT * FROM {table}"
#         else:
#             union += f" UNION ALL SELECT * FROM {table}"
    
#     con.execute(f"CREATE OR REPLACE TABLE all_listings AS {union}")
# else:
#     print("No CSVs found.")