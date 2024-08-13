#!/usr/bin/python3

import sys
import signal
import re

# Initialize variables
total_file_size = 0
status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
line_count = 0

# Regular expression pattern to match the expected log format
log_pattern = re.compile(r'\S+ - \[\S+\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)')

def print_stats():
    """Prints the accumulated statistics"""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    """Handles the SIGINT signal (CTRL + C)"""
    print_stats()
    sys.exit(0)

# Register the signal handler for SIGINT
signal.signal(signal.SIGINT, signal_handler)

# Read from stdin line by line
try:
    for line in sys.stdin:
        match = log_pattern.match(line)
        if match:
            status_code, file_size = match.groups()
            total_file_size += int(file_size)
            if status_code in status_codes:
                status_codes[status_code] += 1

        line_count += 1

        if line_count % 10 == 0:
            print_stats()

except Exception as e:
    pass

# Print remaining stats after the loop ends (in case of incomplete batch)
print_stats()

