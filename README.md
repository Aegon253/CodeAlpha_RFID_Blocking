# RFID Blocking Application

## Overview
This RFID blocking application simulates the process of scanning RFID tags and determining whether they are authorized to access a system. If the tag is unauthorized, it is blocked, and the attempt is logged. The application uses a pre-defined list of allowed tags from a JSON file and logs all events (both successful and unsuccessful attempts) to a log file for audit purposes.

## Features
- **RFID Tag Scanning:** The application scans tags and checks them against a list of allowed tags.
- **Access Control:** If the tag is in the allowed list, access is granted; otherwise, access is denied, and the tag is blocked.
- **Logging:** All actions are logged, including authorized access, unauthorized attempts, and any errors. Logs are stored in a file called `rfid_access.log`.
- **JSON Configuration:** The list of allowed tags is loaded from a JSON file (`allowed_tags.json`).

## Requirements
- Python 3.x
- `logging` module (part of Python standard library)
- JSON file containing allowed tags (`allowed_tags.json`)

## Setup
1. **Install Python:** Make sure you have Python 3.x installed on your system.
2. **Create JSON File:** Create a file named `allowed_tags.json` in the same directory as the script. The structure should look like this:
    ```json
    {
      "allowed_tags": ["12345", "67890", "11223", "44556", "78901"]
    }
    ```

3. **Run the Application:**
   - Clone or download the script.
   - Run the application using the following command:
     ```bash
     python RFID_blocker.py
     ```

## How it Works
1. **Tag Scanning:** The `RFIDReader` class scans RFID tags using the `scan_tag` method. 
2. **Access Verification:** If the scanned tag's ID matches an ID from the allowed tags list, access is granted. Otherwise, the tag is blocked and logged as unauthorized.
3. **Blocking Unauthorized Tags:** Unauthorized tag IDs are blocked, and the incident is logged as an error in the `rfid_access.log` file.
4. **Logging:** All actions (access granted, access denied, and errors) are logged with timestamps.

## Log File Example (`rfid_access.log`)
```log
2024-09-19 12:34:56,789 - INFO - Scanning tag ID: 54321
2024-09-19 12:34:56,790 - WARNING - Access Denied for Tag ID: 54321
2024-09-19 12:34:56,790 - ERROR - Blocking Tag ID: 54321 - Unauthorized access detected!
2024-09-19 12:34:56,791 - ERROR - Unauthorized access attempt by Tag ID: 54321
