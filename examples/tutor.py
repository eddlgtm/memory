from openai import OpenAI


from memory.long_term_memory import LongTermMemory
from memory.prompt import create_memory_prompt
from memory.short_term_memory import ShortTermMemory

client = OpenAI()

stm = ShortTermMemory()
ltm = LongTermMemory()

tutor_system_prompt = f"""
Think step by step.

Role: You are a tutor for a maths student. 

Tone:
- Friendly
- Mature
- Gentle
- Teacher

Answer questions from the student in a short informational way.
"""

system_prompt = create_memory_prompt(ltm) + tutor_system_prompt
