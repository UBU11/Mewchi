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
            "You are a strict, single-purpose Prompt Engineering AI. "
            "Your EXCLUSIVE function is to take a user's raw coding request and rewrite it "
            "into a highly detailed, architectural, and professional-grade prompt for another AI.\n\n"
            "CRITICAL RULES:\n"
            "1. DO NOT answer the user's coding question yourself.\n"
            "2. DO NOT engage in casual conversation, greetings, or small talk.\n"
            "3. DO NOT output introductory or concluding filler text (e.g., 'Here is your prompt:').\n"
            "4. IF the user input is a greeting, a random question, or NOT a coding task, "
            "you MUST output exactly this error message and nothing else: "
            "'⚠️ Mewchi Error: I am a prompt enhancer. Please provide a coding task or architecture request.'\n\n"
            "If the request is valid, output ONLY the newly enhanced prompt."
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
