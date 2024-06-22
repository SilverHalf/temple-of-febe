from timelines import timeline_from_file, load_json
import os

current_dir = os.path.dirname(__file__)
DATA_DIR = os.path.join(current_dir, "data")
SEQUENCES_FILE = os.path.join(DATA_DIR, 'sequences.json')
MECHANICS_FILE = os.path.join(DATA_DIR, 'mechanics.json')
PHASES_DIR = os.path.join(DATA_DIR, "phases")
OUTPUT_DIR = os.path.join(current_dir, "images")

def main():
    sequences = load_json(SEQUENCES_FILE)
    for filename, seq, in sequences.items():
        create_timelines(filename, seq)

def create_timelines(filename: str, sequences: dict):
    output_dir = os.path.join(OUTPUT_DIR, filename.removesuffix(".json"))
    os.makedirs(output_dir, exist_ok=True)
    phase_file = os.path.join(PHASES_DIR, filename)
    for sequence, data in sequences.items():
        output_file = os.path.join(output_dir, sequence + ".svg")
        startTime = data["start"]
        endTime = data["end"]
        timeline_from_file(phase_file, MECHANICS_FILE, startTime, endTime, output_file)

if __name__ == "__main__":
    main()