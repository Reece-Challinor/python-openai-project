import os
import openai
import yaml
from dotenv import load_dotenv
from src.log_manager import logger

# Load environment variables
load_dotenv(dotenv_path=".env")

# Load configuration from config.yaml
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Set the OpenAI API key from the environment
openai.api_key = os.environ.get("OPENAI_API_KEY")

def send_request_to_openai(prompt, model=None, temperature=None, max_tokens=None):
    """
    Send a prompt to the OpenAI chat completion API and return the response.

    Args:
        prompt (str): The user's prompt message.
        model (str, optional): The OpenAI model to use. Defaults to the model in config.yaml if not provided.
        temperature (float, optional): Sampling temperature. Defaults to value in config.yaml if not provided.
        max_tokens (int, optional): Maximum tokens for the response. Defaults to value in config.yaml if not provided.

    Returns:
        str: The response content from the OpenAI model or an error message if something goes wrong.
    """
    model = model or config["openai"]["default_model"]
    temperature = temperature if temperature is not None else config["openai"]["default_temperature"]
    max_tokens = max_tokens if max_tokens is not None else config["openai"]["default_max_tokens"]

    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=temperature
        )
        text_response = response.choices[0].message['content'].strip()
        logger.info(f"OpenAI request success | Prompt snippet: '{prompt[:60]}' | Response snippet: '{text_response[:60]}'")
        return text_response
    except Exception as e:
        logger.error(f"OpenAI request failed: {str(e)}")
        return f"Error: {str(e)}"
