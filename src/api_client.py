import os
import openai
import yaml
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")
from src.log_manager import logger

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

openai.api_key = os.environ.get("OPENAI_API_KEY")

def send_request_to_openai(prompt, model=None, temperature=None, max_tokens=None):
    model = model or config["openai"]["default_model"]
    temperature = temperature if temperature is not None else config["openai"]["default_temperature"]
    max_tokens = max_tokens if max_tokens is not None else config["openai"]["default_max_tokens"]

    from src.log_manager import logger
    try:
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature
        )
        text_response = response.choices[0].text.strip()
        logger.info(f"OpenAI request success | Prompt snippet: {prompt[:60]} | Response snippet: {text_response[:60]}")
        return text_response
    except Exception as e:
        logger.error(f"OpenAI request failed: {str(e)}")
        return f"Error: {str(e)}"
