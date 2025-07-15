import json
from pathlib import Path
import time

from memory.short_term_memory import ShortTermMemory


class LongTermMemory:
    """
    A class for long term memory
    """
    def __init__(self, file_path: Path):
        self.file_path = file_path
        if file_path.is_file():
            with open(file=file_path, mode="w") as f:
                self.memory = json.loads(f)
        else:
            self.memory = {}

    def add_short_term_memory(self, memory: ShortTermMemory):
        self.memory.append({time.gmtime(): memory})

    def save(self):
        with open(file=self.file_path, mode="w") as f:
            f.writelines(json.dumps(self.memory))