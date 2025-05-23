from models.note import Note

# Simulated in-memory database
notes_db = []
 
import json
import os
from models.note import Note

DB_FILE = "notes_data.json"

# Load existing notes from JSON file
def load_notes():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            data = json.load(f)
            return [Note(**item) for item in data]
    return []

# Save notes to JSON file
def save_notes(notes):
    with open(DB_FILE, "w") as f:
        json.dump([note.__dict__ for note in notes], f, indent=2)

# In-memory notes list
notes_db = load_notes()
