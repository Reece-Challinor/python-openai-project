import os
from flask import Flask, request, render_template
from dotenv import load_dotenv
from src.api_client import send_request_to_openai
from src.prompt_manager import build_contextual_prompt
from src.db_manager import save_interaction
from src.log_manager import logger

load_dotenv()
app = Flask(__name__)

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
