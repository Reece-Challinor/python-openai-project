# python-openai-project

A Python Flask application integrating OpenAI's API and Pinecone for text embedding and retrieval.

## Table of Contents
- [python-openai-project](#python-openai-project)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Clone the Repository](#clone-the-repository)
    - [Create a Virtual Environment](#create-a-virtual-environment)
    - [Install Dependencies](#install-dependencies)
    - [Set Up Environment Variables](#set-up-environment-variables)
  - [Usage](#usage)
  - [Project Structure](#project-structure)
    - [run.py](#runpy)
    - [src](#src)
    - [templates](#templates)
    - [static](#static)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)

## Introduction

The **python-openai-project** is a web application built with Python and Flask that demonstrates the integration of OpenAI's GPT models and Pinecone for vector storage and similarity search. The project allows users to input prompts, processes them to build contextual responses, and utilizes Pinecone for storing and querying text embeddings.

## Features

- **Flask Web Application**: A user-friendly web interface built with Flask.
- **OpenAI Integration**: Generates responses using OpenAI's GPT models.
- **Pinecone Vector Store**: Stores and retrieves text embeddings for context-aware responses.
- **Contextual Prompt Building**: Enhances user prompts with relevant context.
- **Logging and Interaction Tracking**: Logs interactions and saves them for future reference.
- **Modular Architecture**: Organized codebase for scalability and maintainability.

## Installation

### Prerequisites

- Python 3.6 or higher
- Pip package manager
- OpenAI API key
- Pinecone API key and environment

### Clone the Repository

```bash
git clone https://github.com/yourusername/python-openai-project.git
cd python-openai-project
```

### Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
python -m venv venv
```

Activate the virtual environment:

- On Windows:

  ```bash
  venv\Scripts\activate
  ```

- On macOS/Linux:

  ```bash
  source venv/bin/activate
  ```

### Install Dependencies

Install the required packages using pip:

```bash
pip install -r requirements.txt
```

### Set Up Environment Variables

Create a `.env` file in the root directory and add your OpenAI and Pinecone API keys:

```env
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENVIRONMENT=your_pinecone_environment
```

## Usage

Run the Flask application with the following command:

```bash
python run.py
```

The application will be accessible at `http://localhost:5000/`.

## Project Structure

```
python-openai-project/
├── run.py
├── requirements.txt
├── src/
│   ├── ui_components/
│   │   └── flask_app.py
│   ├── api_client.py
│   ├── vector_store.py
│   ├── db_manager.py
│   ├── log_manager.py
│   └── prompt_manager.py
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   ├── js/
│   └── images/
└── README.md
```

### run.py

The main entry point of the application that initializes the Flask app and starts the server.

### src

Contains the core modules of the application.

- `ui_components/flask_app.py`: Defines the Flask app and routes.
- `api_client.py`: Handles communication with the OpenAI API.
- `vector_store.py`: Manages interactions with Pinecone for storing and retrieving text embeddings.
- `db_manager.py`: Manages database operations.
- `log_manager.py`: Handles logging of interactions and events.
- `prompt_manager.py`: Builds and processes user prompts.

### templates

Contains HTML templates used by the Flask application.

- `index.html`: The homepage template.

### static

Holds static files like CSS, JavaScript, and images.

- `css/`: Stylesheets.
- `js/`: JavaScript files.
- `images/`: Image assets.

## Contributing

Contributions are welcome. Please create a fork of the repository and submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

For any questions or suggestions, please contact the repository owner.
