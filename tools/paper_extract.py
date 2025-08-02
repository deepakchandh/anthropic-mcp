import json
import os

PAPER_DIR = "papers"

def extract_info(paper_id: str) -> dict:
    for topic_dir in os.listdir(PAPER_DIR):
        topic_path = os.path.join(PAPER_DIR, topic_dir)
        file_path = os.path.join(topic_path, "papers_info.json")
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                try:
                    data = json.load(f)
                    if paper_id in data:
                        return data[paper_id]
                except json.JSONDecodeError:
                    continue
    raise FileNotFoundError(f"Paper ID '{paper_id}' not found.")
