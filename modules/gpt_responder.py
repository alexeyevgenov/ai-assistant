import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_gpt_response(prompt, system_prompt="You are a helpful voice assistant."):
    print("[GPT-4] Generating response...")
    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()
