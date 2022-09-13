# Datamodel Parser
## Intention of this project
When working with external data from APIs, CSV files or database requests often Data Engineers have to store data temporarily in Pandas or Dask DataFrames before pushing these data to other databases.
It's best practice to declare all data types for the dataframe to avoid exceptions later on. The process of creating a data table, read information into a DataFrame and store it back into a database come with some drawbacks:

Data Engineers have to define:
1. A SQL query to create a database table if not exist with all columns and data types defined
2. All data types for the input into a DataFrame
3. SQL data types for Dask and pandas (not mandatory) for writing these information into a data table

For a proof of concept or while development there can be three separate files which define the data types from bullet points 1-3.

When it comes to scaling there has to be another way of putting all these data type information into on single file.

This project is an attempt to solve this problem.

## Definition of JSON File
The JSON File for this project has to have to following syntax:
```
{
    "schema": "your_schema",
    "table_name": "your_table_name",
    "datamodel": [
    {"name": "primary_id", "type": "STRING", "mode": "REQUIRED"},
    {"name": "sales", "type": "INTEGER", "mode": "REQUIRED"},
    {"name": "top_compaign", "type": "BOOLEAN", "mode": "NULLABLE"}
    ],
    "hash_list": [
        "GDPR_NAME",
        "GDPR_PHONE_NUMBER"
    ],
    "special_hashing": ["email"],
    "primary_key": "primary_id"
}
```
## Working with this framework
This framework is still in an alpha phase / under development! Code in short:
```
from data_parser import Handler

if __name__ == "__main__":
    data_model = Handler("/datamodel/datamodel.json")
    primary_key = data_model.get_primary_key()
    hash_list = data_model.get_hash_list()
    special_hash_list = data_model.get_hash_list()
    pandas_output_model = data_model.get_dataframe_output_model()
    pandas_model = data_model.make_dataframe_model()
    sql_command = data_model.make_sql_model()
```
