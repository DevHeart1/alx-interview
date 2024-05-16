#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics
"""
import random
import sys
from time import sleep
import datetime


def print_stats(file_size, status_codes):
    """
    Print the statistics
    """
    for i in range(10000):
        sleep(random.random())
        sys.stdout.write(
            "{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n"
            .format(
                random.randint(1, 255), random.randint(1, 255),
                random.randint(1, 255), random.randint(1, 255),
                datetime.datetime.now(),
                random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
                random.randint(1, 1024)))
        sys.stdout.flush()


def main():
    """
    Main function
    """
    file_size = 0
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    count = 0
    stats = {k: 0 for k in status_codes}

    def print_statistics():
        print("File size: {:d}".format(file_size))
        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                sc = data[-2]
                if sc in stats:
                    stats[sc] += 1
            except (IndexError, KeyError):
                pass
            try:
                file_size += int(data[-1])
            except (TypeError, IndexError, ValueError):
                pass
            if count % 10 == 0:
                print_statistics()
        print_statistics()
    except KeyboardInterrupt:
        print_statistics()
        raise


if __name__ == "__main__":
    main()
