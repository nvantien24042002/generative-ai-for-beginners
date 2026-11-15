
import os
from google import genai
from google.genai import types

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Chưa tìm thấy GEMINI_API_KEY")

client = genai.Client(
    api_key=api_key,
    http_options=types.HttpOptions(
        timeout=30000,
        retry_options=types.HttpRetryOptions(attempts=1)
    )
)

try:
    print("Dang ket noi Gemini...", flush=True)

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents="Xin chào! Hãy trả lời bằng một câu tiếng Việt."
    )

    print("========== GEMINI RESPONSE ==========")
    print(response.text)

except Exception as error:
    print(f"LOI: {type(error).__name__}: {error}")

finally:
    client.close()
