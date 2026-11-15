
import os
from google import genai
from google.genai import types

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Chua tim thay GEMINI_API_KEY")

client = genai.Client(
    api_key=api_key,
    http_options=types.HttpOptions(
        timeout=30000,
        retry_options=types.HttpRetryOptions(attempts=1)
    )
)

try:
    print("Danh sach model ho tro generateContent:\n")

    for model in client.models.list():
        methods = model.supported_actions or []

        if "generateContent" in methods:
            print(model.name)

except Exception as error:
    print(f"ERROR: {type(error).__name__}: {error}")

finally:
    client.close()
