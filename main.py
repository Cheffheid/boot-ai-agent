import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

def main():
    api_key = get_api_key()
    args    = sys.argv[1:]
    prompt  = get_prompt(args)

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    ai_client = genai.Client(api_key=api_key)

    model = 'gemini-2.0-flash-001'
    prompt = args[0]

    response = ai_client.models.generate_content(
        model=model, contents=messages
    )

    print(response.text)

    if is_verbose(args):
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

def get_api_key():
    api_key = os.environ.get("GEMINI_API_KEY")

    return api_key

def get_prompt(args):
    try:
        return args[0]
    except IndexError:
        print("Please provide a prompt!")
        exit(1)

def is_verbose(args):
    return '--verbose' in args

if __name__ == "__main__":
    main()
