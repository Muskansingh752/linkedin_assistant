from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("API key not found")


def generate_linkedin_draft(topic:str):
    client = genai.Client(api_key=api_key)

    prompt = (
        f"You are a busy, highly technical software engineer and startup founder writing a LinkedIn post about: {topic}.\n\n"
        "Follow these strict rules:\n"
        "1. ZERO FLUFF: Tech professionals do not read poetry. Get straight to the point in the very first sentence. No dramatic or philosophical introductions.\n"
        "2. SCANNABLE FORMAT: No long paragraphs. Use short, punchy sentences. Use a bulleted list to highlight the tech stack, the architecture, or the core problem solved.\n"
        "3. EXECUTIVE TONE: Write like a pragmatic senior developer sharing a concrete win. Focus on the execution, the backend logic, and the real-world value.\n"
        "4. BANNED WORDS: Absolutely NO poetic or typical AI buzzwords. DO NOT use: 'journey', 'realm', 'tapestry', 'symphony', 'delve', 'thrilled', 'navigating', 'landscape', 'dive deep', or 'testament'.\n"
        "5. LENGTH: Keep the entire post extremely concise (under 100 words). Add 2-3 highly relevant hashtags at the bottom."

        )

    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt
    )
    return response.text

