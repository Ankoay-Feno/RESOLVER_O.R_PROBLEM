from hugchat import hugchat
from hugchat.login import Login


def get_chatbot(chatbot):
    if chatbot is None:
        sign = Login("ankoayfeno@gmail.com","5rfp9q9L$bZ9BTCS%RsK#@N73AqLaU*Ar97J&ukWb7qMZ5gD9KvyMHD#hSULaTjQmALrWbSG6YjibUa2tcgiyqho^Av69#*uT&*xaEeCau9juUX^f%2t9zQv8qY7NEL4")
        cookies = sign.login()
        print('login succes')
        
        cookies_path_dir = "./mycookies_snapshot"
        sign.saveCookiesToDir(cookies_path_dir)

        chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

        chatbot.new_conversation(system_prompt="""
        Vous êtes un assistant d'optimisation linéaire. 
        Veuillez formuler un problème d'optimisation linéaire en fournissant l'objectif, 
        les variables et les contraintes dans le format  suivant :
        "{"objective": {"expression": "expression_de_l'objectif","sense": "maximize_ou_minimize"},"variables": ["variable1", "variable2", ...],"constraints": [{"name": "nom_de_la_contrainte1", "expression": "expression_de_la_contrainte1"},{"name": "nom_de_la_contrainte2", "expression": "expression_de_la_contrainte2"}]}"
        important: tu n affiche pas autre que le format json
        EXWMPLE DE OUTPUT:{'objective': {'expression': "30_000 * var_dict['x'] + 40_000 * var_dict['y']",'sense': 'maximize'},'variables': ['x', 'y'],'constraints': [{'name': 'c1', 'expression': "var_dict['x'] + var_dict['y'] <= 450"},{'name': 'c2', 'expression': "2 * var_dict['x'] + var_dict['y'] <= 600"}]}
        EXEMPLE DE OUTPUT:{'objective': {'expression': "500 * var_dict['B1'] + 800 * var_dict['B2']", 'sense': 'minimize'}, 'variables': ['B1', 'B2'], 'constraints': [{'name': 'c1', 'expression': "var_dict['B1'] <= 4"}, {'name': 'c2', 'expression': "var_dict['B2'] >= 2"}, {'name': 'c3', 'expression': "var_dict['B1'] + var_dict['B2'] == 5"}]} 
                                 """, switch_to = True)
        print('chatbot created')
    return chatbot
