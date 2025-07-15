from openai import OpenAI
import streamlit as st


from memory.long_term_memory import LongTermMemory
from memory.prompt import create_memory_prompt
from memory.short_term_memory import ShortTermMemory

client = OpenAI()

stm = ShortTermMemory()
ltm = LongTermMemory()

tutor_system_prompt = """
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

st.write("My AI Tutor")

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o-mini"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": "system", "content": system_prompt},
            ],
            stream=True,
        )
        response = st.write_stream(stream)

    st.session_state.messages.append({"role": "assistant", "content": response})

    stm.add_memory({"user_input": prompt, "tutor_response": response})
    print(stm)

ltm.add_short_term_memories(stm)
print(ltm)
