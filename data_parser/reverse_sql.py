import json
import re


class SqlToData:
    def __init__(self, sql_file_location: str):
        self.sql_file_location: str = sql_file_location
        with open(self.sql_file_location, "r") as f_in:
            self.file_content = f_in.read()
