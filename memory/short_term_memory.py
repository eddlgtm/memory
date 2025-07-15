class ShortTermMemory:
    """
    A class for short term memory.
    """

    def __init__(self, memory_limit: int = 20):
        self.memories = []
        self.memory_limit = memory_limit

    def add_memory(self, memory):
        if len(self.memories) >= self.memory_limit:
            self.memories.pop()

        self.memories.insert(0, memory)

    def get_memories(self):
        return self.memories
