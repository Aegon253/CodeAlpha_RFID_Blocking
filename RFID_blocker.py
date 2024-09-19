import time
import random
import json
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('rfid_access.log'), logging.StreamHandler()])

class RFIDTag:
    def __init__(self, tag_id):
        self.tag_id = tag_id

class RFIDReader:
    def __init__(self, allowed_tags):
        self.allowed_tags = allowed_tags

    def scan_tag(self, tag):
        logging.info(f"Scanning tag ID: {tag.tag_id}")
        if tag.tag_id in self.allowed_tags:
            logging.info(f"Access Granted for Tag ID: {tag.tag_id}")
        else:
            logging.warning(f"Access Denied for Tag ID: {tag.tag_id}")
            self.block_tag(tag.tag_id)

    def block_tag(self, tag_id):
        logging.error(f"Blocking Tag ID: {tag_id} - Unauthorized access detected!")
        self.log_unauthorized_access(tag_id)

    def log_unauthorized_access(self, tag_id):
        logging.error(f"Unauthorized access attempt by Tag ID: {tag_id}")

def load_allowed_tags(json_file):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
            return data.get("allowed_tags", [])
    except FileNotFoundError:
        logging.error(f"JSON file '{json_file}' not found!")
        return []
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON file '{json_file}'!")
        return []


if __name__ == "__main__":
    # Load allowed tags from JSON file
    allowed_tags = load_allowed_tags("allowed_tags.json")

    if not allowed_tags:
        logging.error("No allowed tags found. Exiting program.")
    else:
        reader = RFIDReader(allowed_tags)

        # Simulating RFID tags scanning
        for _ in range(5):
            # Randomly generate a tag ID (some will be unauthorized)
            tag_id = str(random.randint(10000, 99999))
            tag = RFIDTag(tag_id)
            reader.scan_tag(tag)
            time.sleep(1)
