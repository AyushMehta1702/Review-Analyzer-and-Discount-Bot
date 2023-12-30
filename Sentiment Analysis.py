import os
import openai

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

while True:
    user_input = input("I'll tell if you are happy or sad!\n Tell me your thinking or feelings:\n" )
    if user_input == "exit" or user_input == "quit":
        break
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are sentiment classification bot, print out the sentiment of user in max upto 5 words"},
            {"role": "user", "content": user_input}
        ],
        temperature=0.7,
        max_tokens=100,
    )

    response_message = response["choices"][0]["message"]
    print(response_message)

