import os
from flask import Flask, request, render_template
from app import get_chatbot
from app import resolve
import json

app = Flask(__name__)

# Initialize global variables
chatbot = None
conversation = []

# Function to initialize the chatbot
def initialize_chatbot():
    global chatbot
    email = os.getenv('CHATBOT_EMAIL')  # Get email from environment variable
    password = os.getenv('CHATBOT_PASSWORD')  # Get password from environment variable
    
    # If email or password is not set in environment variables, prompt user for input
    if email is None or password is None:
        max_attempts = 3
        attempts = 0
        while chatbot is None and attempts < max_attempts:
            try:
                email = input("Enter your email: ")
                password = input("Enter your password: ")
                chatbot = get_chatbot.get_chatbot(None, email, password)  # Initialize chatbot with provided email and password
                os.environ['CHATBOT_EMAIL'] = email  # Store email in environment variable
                os.environ['CHATBOT_PASSWORD'] = password  # Store password in environment variable
            except Exception as e:
                print(f"Connection error: {e}. Please try again.")
                attempts += 1

        # If chatbot is still not initialized after max attempts, exit the application
        if chatbot is None:
            print("Maximum number of attempts reached. The application will close.")
            exit()
    else:
        chatbot = get_chatbot.get_chatbot(None, email, password)  # Initialize chatbot with email and password from environment variables

initialize_chatbot()

# Define the main route for the application
@app.route('/', methods=['GET', 'POST'])
def chat():
    global conversation
    global chatbot
    
    if request.method == 'POST':
        user_input = request.form['message']  # Get user input from form
        
        # Check if chatbot is initialized, if not, initialize it
        if chatbot is None:
            chatbot = get_chatbot.get_chatbot(chatbot)
        print("after chatbot created")
        
        # Get the chatbot's response to the user input
        response = chatbot.chat(user_input)
        print("after chatbot messaging")
        
        # Add the current conversation to the conversation list
        conversation.append({'user': user_input, 'resolved problems': resolve.resolve(json.loads(str(response)))})

    # Render the chat template with the conversation list
    return render_template('chat.html', conversation=conversation)

# Entry point of the application
if __name__ == '__main__':
    if chatbot is None:
        initialize_chatbot()
    app.run(debug=True)  # Run the Flask application in debug mode
