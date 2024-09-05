# Solver of Operational Research

## How to Install

### With Python

1. Create a virtual environment:

    ```sh
    python -m venv your_virtual_name_env
    source your_virtual_name_env/bin/activate
    ```

2. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

### With Docker

1. Build the Docker image:

    ```sh
    docker build -t ImageName:tag .
    ```

## How to Run

### Step 1: Obtain Hugging Face Credentials

The application requires Hugging Face credentials (email and password) for authentication.

### Step 2: Configure and Launch the Application

#### Option A: Run Locally

1. Set the credentials as environment variables:

    ```sh
    export CHATBOT_EMAIL='example@gmail.com'
    export CHATBOT_PASSWORD='password_hugging_face'
    ```

2. Start the application:

    ```sh
    python run.py
    ```

#### Option B: Run in a Docker Container

1. Run the Docker container:

    ```sh
    docker run -it --rm --name containerName -p 5000:5000 ImageName:tag
    ```
