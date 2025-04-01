# Ted Toporkov
# 2024-11-22
# stockprices.py

import sys
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from table import Table

def plot_price_history(table):
    """Plot closing prices over time"""
    entries = table.get_entries()
    dates = [entry.date() for entry in entries]
    prices = [entry.close() for entry in entries]

    plt.figure(figsize=(12, 6))
    plt.plot(dates, prices)

    # Format x-axis to show years properly
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    plt.gca().xaxis.set_major_locator(mdates.YearLocator(5))  # Show every 5 years

    plt.title('DJIA Closing Prices Over Time')
    plt.xlabel('Year')
    plt.ylabel('Price ($)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    if len(sys.argv) != 2:
        print("Usage: python stockprices.py djia.csv")
        sys.exit(1)

    filename = sys.argv[1]
    table = Table(filename)
    plot_price_history(table)

if __name__ == '__main__':
    main()