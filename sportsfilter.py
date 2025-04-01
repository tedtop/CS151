# Ted Toporkov
# 2024-11-07
# sportsfilter.py - Caitlin Clark stats filter and formatter

# Usage: python sportsfilter.py clark.csv offense.txt

import sys
from instream import InStream
from outstream import OutStream

def main(input_file, output_file):
    # Create instances of InStream and OutStream
    instream = InStream(input_file)
    outstream = OutStream(output_file)

    # Write the title centered
    outstream.writeln("        Caitlin Clark Statistics March Madness 2024")
    outstream.writeln()

    # Write the column headers right-aligned with proper spacing
    outstream.writeln("     Date             Opp    FG%   3P   3PA    3P%  AST   PTS")

    # Read header line to get column indices
    header = instream.readLine()
    columns = header.split(',')

    # Process each line in the input file
    while instream.hasNextLine():
        line = instream.readLine()
        data = line.split(',')

        # Extract needed values
        date = data[columns.index('Date')]
        opp = data[columns.index('Opp')]
        fg_pct = float(data[columns.index('FG%')])
        three_p = data[columns.index('3P')]
        three_pa = data[columns.index('3PA')]
        three_p_pct = float(data[columns.index('3P%')])
        ast = data[columns.index('AST')]
        pts = data[columns.index('PTS')]

        # Format each line with proper spacing and right alignment
        formatted_line = (f"{date:>9} {opp:>15} {fg_pct:>6.3f} {three_p:>4} {three_pa:>5} "
                        f"{three_p_pct:>6.3f} {ast:>4} {pts:>5}")
        outstream.writeln(formatted_line)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python sportsfilter.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)