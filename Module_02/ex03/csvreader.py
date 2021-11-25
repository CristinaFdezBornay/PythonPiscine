from __future__ import annotations
import csv
from typing import List, Union

class CsvReader():
    __slots__= ('filename', 'sep', 'header_bool', 'skip_top', 'skip_bottom', 'csvfile_obj',
                'csvfile_reader', 'header', 'data', 'nbr_fields', 'len_records', 'exception')

    def __init__(self, filename:str=None, sep:str=',', header:bool=False, skip_top:int=0, skip_bottom:int=0) -> None:
        self.filename = filename
        self.sep = sep
        self.header_bool = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.csvfile_obj = None
        self.csvfile_reader = None
        self.header = None
        self.data = None
        self.nbr_fields = False
        self.len_records = []
        self.exception = False

    def __enter__(self) -> Union[CsvReader, None]:
        try:
            self.csvfile_obj = open(self.filename, 'r')
            self.csvfile_reader = csv.reader(self.csvfile_obj, delimiter=self.sep)
            return self
        except Exception as exception:
            self.exception = True
            self.__exit__(type=exception.__class__.__name__, value=exception, traceback=exception.__traceback__)
            exit()

    def __exit__(self, type:str=None, value:Exception=None, traceback=None) -> None:
        if self.exception == True:
            if traceback:
                self.__print_traceback__(traceback)
            print("[{}] {}".format(type if type else "ERROR", value if value else ""))
        self.csvfile_obj.close()

    def __print_traceback__(self, traceback) -> (str, str, str):
        tb_splitted = traceback.tb_frame.__str__().strip('<>').split(', ')
        file = str.capitalize(tb_splitted[1])
        line = str.capitalize(tb_splitted[2])
        code = str.capitalize(tb_splitted[3])
        print("Traceback (most recent call last):")
        print("\t{}, {}, {}".format(file, line, code))

    def __set_params__(self, row):
        raw_data = []
        self.nbr_fields = len(row)
        if self.header_bool:
            self.header = row
            next_row = next(self.csvfile_reader)
            self.len_records = list(len(record) for record in next_row)
            raw_data.append(next_row)
        else:
            self.len_records = list(len(record) for record in row)
            raw_data.append(row)
        return raw_data

    def __check_row_corrupted__(self, row):
        if len(row) != self.nbr_fields:
            return True
        if (self.len_records != list(len(record) for record in row)):
            return True

    def getdata(self) -> Union(List, None):
        """ Retrieves the data/records from skip_top to skip bottom.
        Returns:
        nested list(list(list, list, ...)) representing the data.
        """
        try:
            for i, row in enumerate(self.csvfile_reader):
                if i == 0:
                    raw_data = self.__set_params__(row)
                elif self.__check_row_corrupted__(row) == True:
                    raise ValueError("The file is corrupted")
                else:
                    raw_data.append(row)
            self.data = list(map(list, zip(*raw_data)))
            return self.data
        except Exception as exception:
            self.exception = True
            self.__exit__(type=exception.__class__.__name__, value=exception, traceback=exception.__traceback__)
            return None

    def getheader(self) -> List[str]:
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        if self.header_bool:
            return self.header

