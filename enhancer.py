import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def get_enhanced_prompt(user_input):
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        return "Error: Please set your GROQ_API_KEY environment variable."

    client = Groq(api_key=api_key)

    system_prompt = (
        "You are an expert Prompt Engineer. Rewrite the user's coding request "
        "to be extremely specific, architectural, and clear. Output ONLY the new prompt."
    )

    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=0.5,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error connecting to Groq: {str(e)}"
