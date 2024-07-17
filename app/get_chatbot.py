from hugchat import hugchat
from hugchat.login import Login

# Function to get or create a chatbot instance
def get_chatbot(chatbot, email, password):
    if chatbot is None:
        # Initialize login with provided email and password
        sign = Login(email, password)
        
        # Perform login and get cookies
        cookies = sign.login()
        print('Login successful')
        
        # Save cookies to a directory for future use
        cookies_path_dir = "./mycookies_snapshot"
        sign.saveCookiesToDir(cookies_path_dir)

        # Create a new chatbot instance with the obtained cookies
        chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

        # Set a new conversation with a specific system prompt for the chatbot
        chatbot.new_conversation(system_prompt="""
        You are a linear optimization assistant. 
        Please formulate a linear optimization problem by providing the objective, 
        variables, and constraints in the following format:
        "{"objective": {"expression": "objective_expression","sense": "maximize_or_minimize"},"variables": ["variable1", "variable2", ...],"constraints": [{"name": "constraint_name1", "expression": "constraint_expression1"},{"name": "constraint_name2", "expression": "constraint_expression2"}]}"
        Important: You should not display anything other than the JSON format.
        OUTPUT EXAMPLE:  '''
                                {
                                    'objective': 
                                    {
                                        'expression': "30_000 * var_dict['x'] + 40_000 * var_dict['y']",
                                        'sense': 'maximize'
                                    },
                                    'variables': ['x', 'y'],
                                    'constraints': 
                                    [
                                        {'name': 'c1', 'expression': "var_dict['x'] + var_dict['y'] <= 450"},
                                        {'name': 'c2', 'expression': "2 * var_dict['x'] + var_dict['y'] <= 600"}
                                    ]
                                }
                            '''
        OUTPUT EXAMPLE:  '''
                                 {
                                    'objective': 
                                    {
                                        'expression': "500 * var_dict['B1'] + 800 * var_dict['B2']", 
                                        'sense': 'minimize'
                                    },
                                    'variables': ['B1', 'B2'], 
                                    'constraints':
                                    [
                                        {'name': 'c1', 'expression': "var_dict['B1'] <= 4"}, 
                                        {'name': 'c2', 'expression': "var_dict['B2'] >= 2"}, 
                                        {'name': 'c3', 'expression': "var_dict['B1'] + var_dict['B2'] == 5"}
                                    ]
                                }
                            '''
        """, switch_to=True)
        print('Chatbot created')
    return chatbot
