"""
parse_log.py

Parses a ZooKeeper log file and extracts structured fields such as:
- timestamp
- log level
- thread name
- message text
- client IP (if present)
- session ID (if present)

Outputs a CSV file in the output/ directory.
"""

import re
import csv

# Paths to input log file and output CSV
logfile = "/Users/alidavies/Documents/Python/zookeeper_log_analysis/data/zookeeper.log"
outfile = "/Users/alidavies/Documents/Python/zookeeper_log_analysis/output/parsed.csv"

# Regex to match standard ZooKeeper log lines:
# timestamp, log level, thread name, and message
pattern = re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3})\s*-?\s*'r'(INFO|WARN|ERROR)\s*\[([^\]]+)\]\s*-?\s*(.*)$')

# Regex to extract client IP and session ID if present in the message
ip_pattern = re.compile(r'/(\d+\.\d+\.\d+\.\d+):\d+')
session_pattern = re.compile(r'session 0x([0-9a-fA-F]+)')


def main():
    # Open the log file for reading and CSV for writing
    with open(logfile, "r") as f, open(outfile, "w", newline="") as out:
        writer = csv.writer(out)

        # Write CSV header
        writer.writerow(["timestamp", "level", "thread", "message", "client_ip", "session_id"])

        # Process each line in the log file
        for line in f:
            match = pattern.match(line)

            # Only process lines that match the expected log format
            if match:
                timestamp, level, thread, message = match.groups()

                # Optional fields: may or may not be present
                ip_match = ip_pattern.search(message)
                session_match = session_pattern.search(message)

                client_ip = ip_match.group(1) if ip_match else ""
                session_id = session_match.group(1) if session_match else ""

                # Write parsed fields to CSV
                writer.writerow([timestamp, level, thread, message, client_ip, session_id])


if __name__ == "__main__":
    main()

