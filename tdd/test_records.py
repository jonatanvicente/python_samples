import unittest
from datetime import date
from RecordsByDate import RecordsByDate

class TestRecordsByDate(unittest.TestCase):
    def test_load_csv(self):
        records = RecordsByDate.read_csv('test_data.csv')
        expected = {
            'date': '2020-11-30',
            'email': 'alpha@pp.com',
            'status': 'active',
            'source': 'facebook'
        }
        actual = records[date(2020, 11, 30)]
        self.assertEqual(expected, actual)

