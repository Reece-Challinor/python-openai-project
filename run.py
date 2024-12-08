from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")  # Explicitly specifying the path that worked for you

from src.ui_components.flask_app import app

if __name__ == "__main__":
    app.run(debug=True)
