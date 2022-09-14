import json
import re


class SqlToData:
    def __init__(self, sql_file_location: str):
        self.sql_file_location: str = sql_file_location
        with open(self.sql_file_location, "r") as f_in:
            self.file_content = f_in.read()

    def get_primary_key(self) -> str:
        pattern_inline = re.compile("(\w.* primary key)")
        pattern_end_of_command = re.compile(".* primary key\s?\((\w.*)\)")
        raw_data = self.file_content.lower()
        result = re.findall(pattern_inline, raw_data)
        if len(result) > 0:
            return result[0].strip().split(" ")[0]

        result = re.findall(pattern_end_of_command, raw_data)
        if len(result) > 0:
            return result[0]

    def get_datetime_information(self) -> list:
        raw_data = self.file_content.lower()
        date_patter = re.compile("(\w.*)\s?(date|datetime|timestamp)")
        result = re.findall(date_patter, raw_data)
        return [x[0].strip() for x in result]
