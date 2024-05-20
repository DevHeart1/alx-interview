#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""
import sys

def main():
    """
    Main function
    """
    file_size = 0
    count = 0
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in status_codes}

    def print_statistics():
        """
        Print the accumulated statistics
        """
        print("File size: {:d}".format(file_size))
        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                # Assuming the status code is the second-to-last element
                sc = data[-2]
                if sc in stats:
                    stats[sc] += 1
            except (IndexError, KeyError):
                pass
            try:
                # Assuming the file size is the last element
                file_size += int(data[-1])
            except (IndexError, ValueError):
                pass

            if count % 10 == 0:
                print_statistics()

        print_statistics()

    except KeyboardInterrupt:
        print_statistics()
        raise

if __name__ == "__main__":
    main()
