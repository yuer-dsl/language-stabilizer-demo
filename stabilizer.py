# stabilizer.py
# Minimal non-intervention Language Stabilizer wrapper
# Author: Yuer

from openai import OpenAI

client = OpenAI()

def apply_language_stabilizer(user_input: str, model="gpt-4.1-mini"):
    """Wraps the stabilizer prompt around any user input.
    This module does NOT provide advice, therapy, or assessment.
    """
    with open("prompts/stabilizer_v0.2.txt", "r", encoding="utf-8") as f:
        stabilizer_prompt = f.read()

    final_prompt = (
        stabilizer_prompt
        + "\n\n---\nUser: "
        + user_input
    )

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": final_prompt}],
        temperature=0.0
    )

    return response.choices[0].message["content"]
