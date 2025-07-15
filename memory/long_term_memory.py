import json
from pathlib import Path
from time import time

from dotenv import load_dotenv
from openai import OpenAI

from memory.short_term_memory import ShortTermMemory

load_dotenv()


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
        self.client = OpenAI()

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
        completion = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": """
                    Role: You are a tool that takes memories in a list and returns a description of these memories to be used by another LLM in its context.

                    Tone:
                    - Do not respond with specifics about time stamps
                    - Aggregate the memories into a succinct paragraph
                    - Do not mention your role in doing this, just return the memory summary
                    """,
                },
                {"role": "user", "content": f"{self.memory}"},
            ],
        )

        self.summary = completion.choices[0].message.content
