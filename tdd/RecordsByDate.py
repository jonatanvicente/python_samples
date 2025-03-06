import csv

from dateutil.parser import parse as parse_datetime

class RecordsByDate:
    def __init__(self, data):
        print('**** Constructor')
        self.data = data

    @classmethod
    def read_csv(cls, path):
        print('**** Method read_csv')
        data = {}
        with open(path) as handle:
            for row in csv.DictReader(handle):
                when = parse_datetime(row['date']).date()
                data[when] = row
        return cls(data)

    # This method allows instances of the class to use the bracket notation (e.g., records[date])
    # to access data stored in the data attribute.It retrieves the value associated with the given
    # when key from the data dictionary.

    def __getitem__(self, when):
        print('**** Method __getitem__')
        return self.data[when]