# Ted Toporkov
# 2024-11-22
# entry.py

from datetime import datetime

class Entry:
    def __init__(self, line):
        """
        Constructor for Entry class. Takes a CSV line and creates an Entry object.
        Each line format: Date,Open,High,Low,Close,Volume,Adj. Close
        """
        fields = line.strip().split(',')
        # Convert two-digit year to four-digit year (assuming 20xx for our data)
        date_str = fields[0]
        self._date = datetime.strptime(date_str, '%d-%b-%y')
        if self._date.year > 2024:  # If year appears after 2024, it's probably 19xx
            self._date = self._date.replace(year=self._date.year - 100)

        self._open = float(fields[1])
        self._high = float(fields[2])
        self._low = float(fields[3])
        self._close = float(fields[4])
        self._volume = int(fields[5])
        self._adj_close = float(fields[6])

    def date(self): return self._date
    def open(self): return self._open
    def high(self): return self._high
    def low(self): return self._low
    def close(self): return self._close
    def volume(self): return self._volume
    def adj_close(self): return self._adj_close

    def __str__(self):
        """Returns string representation of the entry"""
        return f"{self._date.strftime('%d-%b-%Y')}: Open ${self._open:.2f}, Close ${self._close:.2f}"

def _test():
    """Test client for Entry class"""
    test_line = "17-Mar-06,11294.94,11294.94,11253.23,11279.65,2549619968,11279.65"
    entry = Entry(test_line)
    print(entry)
    print(f"High: ${entry.high():.2f}")
    print(f"Low: ${entry.low():.2f}")

if __name__ == '__main__':
    _test()