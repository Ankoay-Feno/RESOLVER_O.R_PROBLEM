import os
from flask import Flask, request, render_template
from app import get_chatbot
from app import resolve
import json

app = Flask(__name__)

# Initialisation des variables globales
chatbot = None
conversation = []


def initialize_chatbot():
    global chatbot
    email = os.getenv('CHATBOT_EMAIL')
    password = os.getenv('CHATBOT_PASSWORD')
    
    if email is None or password is None:
        max_attempts = 3
        attempts = 0
        while chatbot is None and attempts < max_attempts:
            try:
                email = input("Entrez votre email : ")
                password = input("Entrez votre mot de passe : ")
                chatbot = get_chatbot.get_chatbot(None, email, password)
                os.environ['CHATBOT_EMAIL'] = email
                os.environ['CHATBOT_PASSWORD'] = password
            except Exception as e:
                print(f"Erreur de connexion : {e}. Veuillez réessayer.")
                attempts += 1

        if chatbot is None:
            print("Nombre maximum de tentatives atteint. L'application va se fermer.")
            exit()
    else:
        chatbot = get_chatbot.get_chatbot(None, email, password)

initialize_chatbot()

@app.route('/', methods=['GET', 'POST'])
def chat():
    global conversation
    global chatbot
    
    if request.method == 'POST':
        user_input = request.form['message']
        
        # Vérifie si le chatbot est déjà initialisé, sinon initialise-le
        if chatbot is None:
            chatbot = get_chatbot.get_chatbot(chatbot)
        
        # Obtenez la réponse du chatbot
        response = chatbot.chat(user_input)
        
        # Ajouter la conversation actuelle à la liste des conversations
        conversation.append({'user': user_input, 'bot': str(response)})
        # dict_response = json.loads(str(response))
        # print((dict_response))
    
    return render_template('chat.html', conversation=conversation)


if __name__ == '__main__':
    if chatbot is None:
        initialize_chatbot()
    app.run(debug=True)
