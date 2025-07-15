from memory.long_term_memory import LongTermMemory


def create_memory_prompt(ltm: LongTermMemory):
    return f"""
Data from a previous session has been added as Context below. 
Use this context you consider the next prompt.

Context: {ltm.summary}

"""
