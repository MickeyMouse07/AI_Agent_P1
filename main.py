import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import *
from call_function import available_functions





def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    

    if len(sys.argv) == 1:
        print("AI Code Assistant")
        print("Usage: uv run main.py 'prompt' or ")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    messages = [
    types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
    ]

    generate_content(client,messages)
    
def generate_content(client,messages):
    verbose = "--verbose" in sys.argv 
    response = client.models.generate_content(
    model='gemini-2.0-flash-001', 
    contents=messages,
    config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
    )
    usage = response.usage_metadata

    
    
    for part in response.candidates[0].content.parts:
        if part.function_call:
            print(f"Calling function: {part.function_call.name}({part.function_call.args})")
        elif part.text:
            if verbose:
                print(f"User prompt: {sys.argv[1]}")
                print(f"Prompt tokens: {usage.prompt_token_count}")
                print(f"Response tokens: {usage.candidates_token_count}")
            print("Response:") 
            print(part.text)
            
    
    
    
    
    
    
   




if __name__ == "__main__":
    main()
