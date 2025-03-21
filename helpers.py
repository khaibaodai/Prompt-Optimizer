from google import genai
from google.genai import types
from google.genai import errors
from dotenv import load_dotenv, find_dotenv
import os

# Find and load environment variables
_ = load_dotenv(find_dotenv())

# Set up model and system prompt
MODEL = "gemini-2.0-flash"
SYSTEM_INSTRUCTION = """
Your response will be the optimized prompt only.
Your response will be in English.
But if you see any Vietnamese words in the prompt, you should respond in Vietnamese.
"""

def get_response(prompt):
    """A helper function to generate an optimized prompt using the Gemini API from user input."""
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("API key not found in environment variables")
        
        client = genai.Client(api_key = api_key)

        response = client.models.generate_content(
            model = MODEL,
            contents = prompt,
            config = types.GenerateContentConfig(
                system_instruction = SYSTEM_INSTRUCTION,
                max_output_tokens = 500,
                temperature = 0.5
            )
        )
        return response.text
    except ValueError as e:
        print(f"Config error: {e}")
        raise
    except errors.APIError as e:
        print(f"Gemini API error: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise

def validate_api_key(api_key):
    """Validate the Gemini API key."""
    try:
        client = genai.Client(api_key = api_key)
        response = client.models.generate_content(
            model = MODEL,
            contents = "hello",
            config = types.GenerateContentConfig(max_output_tokens = 10)
        )
        return True
    except Exception as e:
        print(f"API key validation error: {e}")
        return False

def validate_environment():
    """Validate required environment variables exist."""
    required_vars = ["GEMINI_API_KEY"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print(f"ERROR: Missing required environment variables: {', '.join(missing_vars)}")
        print("Please set these variables in your .env file or environment")
        return False
    
    """Validate the Gemini API key."""
    if not validate_api_key(os.getenv("GEMINI_API_KEY")):
        print("ERROR: Invalid Gemini API key")
        return False
    return True