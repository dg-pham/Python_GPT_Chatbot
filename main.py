import os

import openai
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("API_KEY")

openai.api_key = key


def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        user_input = input('You: ')
        if user_input.lower() in ['quit', 'exit']:
            break

        response = chat_with_gpt(user_input)
        print('ChatBot: ', response)

