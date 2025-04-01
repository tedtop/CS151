# Ted Toporkov
# 2024-11-22
# table.py

from entry import Entry
import matplotlib.pyplot as plt
from datetime import datetime

class Table:
    def __init__(self, filename):
        """Constructor reads CSV file and builds array of Entry objects"""
        self._entries = []
        with open(filename, 'r') as file:
            next(file)  # Skip header line
            for line in file:
                self._entries.append(Entry(line))
        self._entries.reverse()  # Make chronological order

    def get_entries(self):
        """Returns the list of entries"""
        return self._entries

    def get_period_avg(self, start_date, end_date, field='close'):
        """Returns average of specified field over given date range"""
        values = []
        for entry in self._entries:
            if start_date <= entry.date() <= end_date:
                if field == 'close':
                    values.append(entry.close())
                elif field == 'open':
                    values.append(entry.open())
                elif field == 'high':
                    values.append(entry.high())
                elif field == 'low':
                    values.append(entry.low())
        return sum(values) / len(values) if values else 0

def _test():
    """Test client for Table class"""
    table = Table('djia.csv')
    start = datetime(1985, 1, 1)
    end = datetime(1985, 12, 31)
    avg = table.get_period_avg(start, end)
    print(f"Average closing price in 1985: ${avg:.2f}")

if __name__ == '__main__':
    _test()