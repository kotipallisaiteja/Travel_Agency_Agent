# backend/ai_agent.py

import os

from dotenv import load_dotenv
from google import genai

from backend.system_prompt import SYSTEM_PROMPT

# Load .env file
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def ask_gemini(question, insights, recommendations):

    prompt = f"""
    {SYSTEM_PROMPT}

    Question:
    {question}

    Business Metrics:
    {insights}

    Recommendations:
    {recommendations}

    IMPORTANT:

    Return the answer exactly like:

    📊 Business Snapshot

    • Point 1
    • Point 2

    🔍 Root Cause Analysis

    • Point 1
    • Point 2

    📈 Future Impact

    • Point 1
    • Point 2

    💡 Recommended Actions

    • Point 1
    • Point 2

    🎯 Executive Verdict

    • Final conclusion

    Use line breaks between every section.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    return response.text