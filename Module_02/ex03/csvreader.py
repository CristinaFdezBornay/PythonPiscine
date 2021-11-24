from __future__ import annotations
import csv
from typing import List, Union

class CsvReader():
    __slots__= ('filename', 'sep', 'header_bool', 'skip_top', 'skip_bottom',
                'csvfile_obj', 'csvfile_reader', 'header', 'data', 'nbr_fields', 'exception')

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
        self.exception = False

    def __enter__(self) -> Union[CsvReader, None]:
        try:
            self.csvfile_obj = open(self.filename, 'r')
            self.csvfile_reader = csv.reader(self.csvfile_obj, delimiter=self.sep)
            return self
        except Exception as exception:
            self.exception = True
            self.__exit__(type=exception.__class__.__name__, value=exception, traceback=exception.__traceback__)
            return None

    def __exit__(self, type:str=None, value:Exception=None, traceback=None) -> None:
        if self.exception == True:
            if traceback:
                print("Traceback:\n{}".format(traceback))
            print("[{}] {}".format(type if type else "ERROR", value if value else ""))
            return
        self.csvfile_obj.close()

    def getdata(self) -> Union(List, None):
        """ Retrieves the data/records from skip_top to skip bottom.
        Returns:
        nested list(list(list, list, ...)) representing the data.
        """
        try:
            i = 0
            raw_data = []
            for row in self.csvfile_reader:
                if i == 0:
                    self.nbr_fields = len(row)
                    if self.header_bool:
                        self.header = row
                elif len(row) != self.nbr_fields:
                    raise ValueError("The file is corrupted")
                else:
                    raw_data.append(row)
                i += 1
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

