#!/usr/bin/python3
"""
Log parsing
"""

import sys

def print_stats(stats: dict, file_size: int) -> None:
    """Print the current statistics."""
    print("File size: {:d}".format(file_size))
    for k, v in sorted(stats.items()):
        if v:
            print("{}: {}".format(k, v))

if __name__ == '__main__':
    fs, count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in codes}

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            if len(data) > 2:
                status_code = data[-2]
                file_size = data[-1]
                if status_code in stats:
                    stats[status_code] += 1
                try:
                    fs += int(file_size)
                except ValueError:
                    pass
            if count % 10 == 0:
                print_stats(stats, fs)
        print_stats(stats, fs)
    except KeyboardInterrupt:
        print_stats(stats, fs)
        raise
