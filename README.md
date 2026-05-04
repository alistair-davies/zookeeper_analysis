# ZooKeeper Log Analysis

This repository contains my personal project for analysing a real ZooKeeper log file.  
The goal is to practise real-world troubleshooting, log parsing, and distributed‑systems investigation using Python.

## 📂 Project Structure

zookeeper_log_analysis/
- data/
  - zookeeper.log
- scripts/
  - (Python scripts for parsing, filtering, and analysing logs)
- output/
  - (Generated CSVs, summaries, or extracted events)

### Folder Descriptions

- **data/**  
  Contains the raw ZooKeeper log file used for analysis.

- **scripts/**  
  Python scripts that parse, filter, and analyse the log file.  
  These scripts extract timestamps, event types, warnings, errors, and other patterns.

- **output/**  
  Any generated CSV files, summaries, extracted events, or analysis results.

## How To Run The Scripts

1. Clone the repository:

   git clone <your-repo-url>

2. Ensure you have Python 3.10+ installed.

3. Navigate to the project folder:

   cd zookeeper_log_analysis

4. Run the parsing script:

   python scripts/parse_log.py

5. Output files will appear in the `output/` folder.

## Scripts Overview

- **parse_log.py**  
  Reads the raw log file and extracts structured fields such as timestamp, log level, thread, message, client IP, and session ID.

## Future Improvements

- Add visualisations for event frequency
- Add regex-based extraction for more event types
- Add summary reports (e.g., WARN per hour, top client IPs)
- Add unit tests for parsing functions


