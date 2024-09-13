import configparser
import pyodbc
import pandas as pd
import sys
from os import path


# Read connection details from config file
config = configparser.ConfigParser()
import os
print(os.getcwd())
try:
    if path.exists(r'config.ini'):
        config.read(r'config.ini')
except configparser.Error as e:
    print(f"Error reading config file: {e}")

# Database connection details from config
server = config['database']['server']
database_name = config['database']['database']
username = config['database']['username']
password = config['database']['password']

# Establish a connection
conn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database_name + ';UID=' + username + ';PWD=' + password
)

# Tables to extract data from (you can also read this from config if needed)
tables = ['tblUser', 'tblStakeholder', 'tblGroup']

# Create an empty DataFrame to store the consolidated data
consolidated_data = pd.DataFrame()

# Extract and transform data from each table
for table in tables:
    query = f'SELECT * FROM {table}'
    df = pd.read_sql(query, conn)

    # Perform any necessary data transformations here (e.g., renaming columns, data cleaning)
    # ...

    # Append the data to the consolidated DataFrame
    consolidated_data = pd.concat([consolidated_data, df], ignore_index=True)

# Close the database connection
conn.close()

# Save the consolidated data to a single file (e.g., CSV)
consolidated_data.to_csv('consolidated_data.csv', index=False)

print("Data extraction and consolidation completed successfully!")