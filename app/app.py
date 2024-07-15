from flask import Flask, request, render_template
from app import get_chatbot
from app import resolve
import json

app = Flask(__name__)

# Initialisation des variables globales
chatbot = None
conversation = []

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
        print(resolve.resolve(json.loads(str(response)))) 
    
    return render_template('chat.html', conversation=conversation)

if __name__ == '__main__':
    app.run(debug=True)

