import json


class JsonToData:
    """
    Handler class with importing JSON information for future pandas and sql processing
    """
    def __init__(self, model_storage_location: str):
        """
        Init method which needs are mandatory for loading JSON information
        Args:
            model_storage_location: str (location of json file)
        """
        self.model_storage_location: str = model_storage_location
        try:
            with open(self.model_storage_location, "r") as f_in:
                self.json_in: json = json.loads(f_in.read())
        except json.decoder.JSONDecodeError:
            print("Error! Problem with JSON file!")

    @staticmethod
    def _datatype_mapping(type_in, target_type: str) -> str:
        if target_type == "dataframe":
            mapping = {
                "string": "str",
                "integer": "int",
                "boolean": "bool",
                "date": "str",
                "datetime": "str",
                "float": "float",
                "numeric": "float",
                "text": "str",
                "smallinteger": "int"
            }
        elif target_type == "sql":
            mapping = {
                "string": "varchar",
                "integer": "int",
                "boolean": "bool",
                "date": "date",
                "datetime": "datetime",
                "float": "float",
                "numeric": "numeric",
                "text": "text",
                "smallinteger": "smallint"
            }
        return mapping[type_in]

    def get_primary_key(self) -> str:
        """
        Method for grabbing primary key information from json file
        Returns: str
        """
        return self.json_in['primary_key']

    def get_hash_list(self) -> list:
        """
        Method for grabbing hash_list information from json file
        Returns: list
        """
        return self.json_in['hash_list']

    def get_special_hash_list(self) -> list:
        """
        Method for grabbing special_hash_list information from json file
        Returns: list
        """
        return self.json_in['special_hashing']

    def get_dataframe_output_model(self) -> list:
        """
        Method for grabbing datamodel information from json file
        Returns: list
        """
        return self.json_in['datamodel']

    def get_datetime_information(self) -> list:
        """
        Method for grabbing date and datetime information from json file and return column names as list
        Returns: list
        """
        datamodel = self.json_in['datamodel']
        return [x['name'] for x in datamodel if x["type"].lower() in ['date', 'datetime']]

    def make_dataframe_model(self) -> dict:
        """
        Method for creating a dictionary with column name and data type for working with pandas data frames
        Returns: dict
        """
        datamodel = self.json_in['datamodel']
        output_list: list = [
            (entry["name"], self._datatype_mapping(entry["type"].lower(), "dataframe")) for entry in datamodel
        ]
        return dict(output_list)

    def make_sql_model(self) -> str:
        """
        Method for creating a SQL command for CREATE TABLE IF NOT EXIST
        Returns: str
        """
        datamodel = self.json_in['datamodel']
        schema = self.json_in['schema']
        table = self.json_in['table_name']
        primary_key = self.get_primary_key()
        if primary_key != "":
            _primary_key_command = f", PRIMARY KEY ({primary_key})"
        else:
            _primary_key_command = ""
        sql_command: str = f"CREATE TABLE IF NOT EXIST {schema}.{table}"
        _temp_table = [f"{entry['name']} {self._datatype_mapping(entry['type'].lower(), 'sql')}" for entry in datamodel]
        return sql_command + f" ({','.join(_temp_table)} {_primary_key_command})"
