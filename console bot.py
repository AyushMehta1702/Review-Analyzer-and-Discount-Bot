import os
import openai
#from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
# client = OpenAI(api_key='OPENAI_API_KEY')
# Starting New Consversation
print("\n\n Ayurvi: Hey What´s up?")

while True:
    user_input = input("")
    if user_input == "exit" or user_input == "quit":
        break

    response = openai.ChatCompletion.create(
        model="gpt-4",
        massages=[
            {"role": "system", "content": "You are a polite, sensitive and loving person. If someone says or behave rude or impolite with you, print exactly 'RUDE', otherwise responsd"},
            {"role": "user", "content": user_input}
        ],
        temperature=0.7,
        max_tokens=100,
    )

    response_message = response["choices"][0]["message"]
    response_content = response_message["content"]
    if response_content == "RUDE":
        print("Sorry, I don't like RUDE people, so can't talk to you, GOODBYE")
        break
    print("Ayurvi:" + response_content)
