import os
from flask import Flask, request, render_template
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")  # Ensure env is loaded if not already
from src.api_client import send_request_to_openai
from src.prompt_manager import build_contextual_prompt
from src.db_manager import save_interaction
from src.log_manager import logger

app = Flask(__name__)

template = """
<!doctype html>
<title>OpenAI Prompt</title>
<h1>Enter your prompt:</h1>
<form method="post">
  <textarea name="prompt" rows="5" cols="50"></textarea><br>
  <input type="submit" value="Submit">
</form>
{% if response %}
  <h2>Response:</h2>
  <pre>{{ response }}</pre>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    response = None
    if request.method == "POST":
        user_prompt = request.form.get("prompt")
        if user_prompt:
            contextual_prompt = build_contextual_prompt(user_prompt)
            response = send_request_to_openai(contextual_prompt)
            save_interaction(user_input=user_prompt, model_response=response)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("FLASK_RUN_PORT", 5000)), debug=True)
