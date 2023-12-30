import os
import openai

from dotenv import load_dotenv
load_dotenv()


def generate_review(review):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system",
             "content": "act as a sentiment classification bot and determine if the user is expressing happiness or dissatisfaction"},

            {"role": "user", "content": review}
        ],
        temperature=0.7,
        max_tokens=150,
    )

    response_message = response["choices"][0]["message"]["content"]
    print(f"OpenAI Response: {response_message}")
    # if response_message == "happy":
    #     return "Thanks for shopping with us, come back soon!"
    # return "Sorry to hear about your experience, We are offering you Discount Code of 20% OFF: "
    #
    #
    # for choice in response["choices"]:
    #     message_content = choice["message"]["content"]
    #     if "sad" in message_content.lower():
    #         return "Thanks for shopping with us, come back soon!"
    #     return "Sorry to hear about your experience, We are offering you Discount Code of 20% OFF: "

    if "happiness" in response_message.lower():
        return "Many Thanks for shopping with us, Come Back Soon!"
    elif "dissatisfaction" in response_message.lower():
        return "Sorry to hear about your experience, We are offering you Discount Code of 20% OFF: MODEZA20"

    # if sentiment_score >= threshold:
    #     return "Thanks for shopping with us, come back soon!"
    # elif 0.4 <= sentiment_score <= 0.6:
    #     return "We appreciate your feedback. If you have any concerns, please let us know."
    # else:
    #     return "Sorry to hear about your experience, We are offering you Discount Code of 20% OFF: "
# Example usage:
