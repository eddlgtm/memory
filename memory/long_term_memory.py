import json
from pathlib import Path
from time import time

from memory.short_term_memory import ShortTermMemory


class LongTermMemory:
    """
    A class for long term memory
    """

    def __init__(self, file_path: Path = Path("./memory.json")):
        self.file_path = file_path

        if file_path.is_file():
            with open(file=file_path, mode="w") as f:
                self.memory = json.loads(f)
        else:
            self.memory = {}

        self.summary = ""

    def __repr__(self):
        return f"{self.memory}"

    def get_memory(self):
        return self.memory

    def add_short_term_memory(self, memory: ShortTermMemory):
        self.memory[round(time())] = memory.get_memories()

    def save(self):
        # We can store memory as a json file for now
        with open(file=self.file_path, mode="w") as f:
            f.writelines(json.dumps(self.memory))

    def summarise(self):
        # We need to take all the memories and condense them into a summary
        # that can be fed to an LLM in its context, maybe with some sort of
        # prioritisation for recent memories
        raise NotImplementedError
