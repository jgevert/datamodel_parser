from data_parser import JsonToData
from data_parser import SqlToData


if __name__ == "__main__":
    # JSON to Data: SQL, DataModel etc
    data_model_from_json = JsonToData("datamodel/datamodel.json")
    primary_key = data_model_from_json.get_primary_key()
    hash_list = data_model_from_json.get_hash_list()
    special_hash_list = data_model_from_json.get_hash_list()
    pandas_output_model = data_model_from_json.get_dataframe_output_model()
    pandas_model = data_model_from_json.make_dataframe_model()
    sql_command = data_model_from_json.make_sql_model()

    # SQL to JSON
    data_model_from_sql = SqlToData("datamodel/create_dummy_data_table.sql")
    print(data_model_from_sql.file_content)
