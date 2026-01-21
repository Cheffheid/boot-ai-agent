import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

def main():
    api_key = get_api_key()
    parser  = get_prompt_parser()
    args    = parser.parse_args()
    prompt  = args.user_prompt

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    ai_client = genai.Client(api_key=api_key)

    model = 'gemini-2.5-flash'

    response = ai_client.models.generate_content(
        model=model, contents=messages
    )

    if response.usage_metadata is not None:

        if args.verbose:
            print(f"User prompt: {prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print(f"Response:")
        print(response.text)
    else:
        raise RuntimeError("There was no usage metadata returned. There was likely an issue interacting with the API.")

def get_api_key():
    api_key = os.environ.get("GEMINI_API_KEY")

    return api_key

def get_prompt_parser():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

    return parser

def is_verbose(args):
    return '--verbose' in args

if __name__ == "__main__":
    main()
