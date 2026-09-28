import json
import os
from patient import Patient

DATA_FILE = os.path.join("data", "patients.json")

def load_patients():
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return [Patient.from_dict(item) for item in data]
    except (json.JSONDecodeError, IOError):
        return []

def save_patients(patients):
    if not os.path.exists("data"):
        os.makedirs("data")
    with open(DATA_FILE, "w") as f:
        json.dump([p.to_dict() for p in patients], f, indent=4)