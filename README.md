# SOLVER OF OPERATIONAL RESEARCH

### HOW TO INSTALL?

• With Python:
    ```
    $ python -m venv your_virtual_name_env
    $ source your_virtual_name_env/bin/activate
    $ pip install -r requirements.txt
    ```
       
• With Docker:
    ```
    $ docker build -t ImageName:tag .
    ```


### HOW TO RUN?

• Step 1:
The application needs the Hugging Face credentials (login with password).

• Step 2:

- Set credentials in the environment:
    ```
    $ export CHATBOT_EMAIL='example@gmail.com'
    $ export CHATBOT_PASSWORD='password_hugging_face'
    $ python run.py  
    ```
- Or run on Docker Container 
    ```
    $ docker run -it --rm --name containerName -p 5000:5000 ImageName:tag
    ```
