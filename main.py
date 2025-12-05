import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import *
from call_function import available_functions, call_function
from config import MAX_ITERS



def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    verbose = "--verbose" in sys.argv 
    args = []
    
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if len(sys.argv) == 1:
        print("AI Code Assistant")
        print("Usage: uv run main.py 'prompt' or ")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]



    iters = 0
    while True:
        iters += 1
        if iters > MAX_ITERS:
            print(f"Maximum iterations ({MAX_ITERS}) reached.")
            sys.exit(1)


        try:
            result = generate_content(client, messages, verbose)
            if result:
                print("Final response:")
                print(result)
                break
        except Exception as e:
            print(f"Error in generate_content: {e}")






    
   
def generate_content(client,messages, verbose):
    response = client.models.generate_content(
    model='gemini-2.0-flash-001', 
    contents=messages,
    config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
    )

    usage = response.usage_metadata


    if verbose:
        print(f"Prompt tokens: {usage.prompt_token_count}")
        print(f"Response tokens: {usage.candidates_token_count}")  


    if response.candidates:
        for candidate in response.candidates:
            function_call_content = candidate.content
            messages.append(function_call_content)


    if not response.function_calls:
        return response.text         

   

    function_responses = []
    for part in response.function_calls:
        result = call_function(part, verbose=verbose)

        if (
            not result.parts
            or not result.parts[0].function_response
        ):
            raise Exception("empty function call result")
        
        if verbose:
            print(f"-> {result.parts[0].function_response.response}")
        function_responses.append(result.parts[0])

    if not function_responses:
        raise Exception("no function responses generated, exiting.")
        
    messages.append(types.Content(role="user", parts=function_responses))


        

            
if __name__ == "__main__":
    main()
