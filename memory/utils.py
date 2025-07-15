from dotenv import load_dotenv
from openai import OpenAI


def send_message(system_prompt="", user_prompt=""):
    load_dotenv()
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": f"""
                {system_prompt}
                """,
            },
            {"role": "user", "content": f"{user_prompt}"},
        ],
    )

    return completion.choices[0].message.content
