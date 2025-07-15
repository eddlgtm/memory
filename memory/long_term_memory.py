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

        self.summary = ""

    def add_short_term_memory(self, memory: ShortTermMemory):
        # Add short term memory to long term memory
        # time stamps as keys organise when they're added
        self.memory.append({time.gmtime(): memory})

    def save(self):
        # We can store memory as a json file for now
        with open(file=self.file_path, mode="w") as f:
            f.writelines(json.dumps(self.memory))

    def summarise(self):
        # We need to take all the memories and condense them into a summary
        # that can be fed to an LLM in its context, maybe with some sort of
        # prioritisation for recent memories
        raise NotImplementedError
