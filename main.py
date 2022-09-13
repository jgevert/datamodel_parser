from data_parser import Handler

if __name__ == "__main__":
    data_model = Handler(r"D:\Code\datamodel_parser\datamodel\datamodel.json")
    primary_key = data_model.get_primary_key()
    hash_list = data_model.get_hash_list()
    special_hash_list = data_model.get_hash_list()
    pandas_output_model = data_model.get_dataframe_output_model()
    pandas_model = data_model.make_dataframe_model()
    sql_command = data_model.make_sql_model()
    print(sql_command)
