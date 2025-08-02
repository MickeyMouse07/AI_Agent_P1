import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types






def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    

    if len(sys.argv) == 1:
        print("Usage: uv run main.py 'prompt' ")
        sys.exit(1)

    messages = [
    types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
    ]

    generate_content(client,messages)





    
def generate_content(client,messages):
    verbose = "--verbose" in sys.argv   
    response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=messages)
    usage = response.usage_metadata
    

    if verbose:
        print(f"User prompt: {sys.argv[1]}")
        print(f"Prompt tokens: {usage.prompt_token_count}")
        print(f"Response tokens: {usage.candidates_token_count}")
    print("Response:")    
    print(response.text)





if __name__ == "__main__":
    main()
