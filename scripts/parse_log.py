import re
import csv

logfile = "/Users/alidavies/Documents/Python/zookeeper_log_analysis/data/zookeeper.log"
outfile = "/Users/alidavies/Documents/Python/zookeeper_log_analysis/output/parsed.csv"

# Single-line regex (no breaks, no continuation)
pattern = re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3})\s*-?\s*(INFO|WARN|ERROR)\s*\[([^\]]+)\]\s*-?\s*(.*)$')

ip_pattern = re.compile(r'/(\d+\.\d+\.\d+\.\d+):\d+')
session_pattern = re.compile(r'session 0x([0-9a-fA-F]+)')

with open(logfile, "r") as f, open(outfile, "w", newline="") as out:
    writer = csv.writer(out)
    writer.writerow(["timestamp", "level", "thread", "message", "client_ip", "session_id"])

    for line in f:
        match = pattern.match(line)
        if match:
            timestamp, level, thread, message = match.groups()

            ip_match = ip_pattern.search(message)
            session_match = session_pattern.search(message)

            client_ip = ip_match.group(1) if ip_match else ""
            session_id = session_match.group(1) if session_match else ""

            writer.writerow([timestamp, level, thread, message, client_ip, session_id])
