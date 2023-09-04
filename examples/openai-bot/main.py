from textbase import bot, Message
from textbase.models import OpenAI
from typing import List

from dotenv import dotenv_values

# Load your OpenAI API key
config = dotenv_values(".env") 
OpenAI.api_key = config["OPEN_AI_KEY"]
#  You are chatting with an AI. There are no specific prefixes for responses, so you can ask or talk about anything you like.
# The AI will respond in a natural, conversational manner. Feel free to start the conversation with any question or topic, and let's have a
# pleasant chat!
# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """"You are a psychologist you have to solve the psychology queries of a user by chatting with them in a conversational manner and also \nby following the below mentioned rules these rules should be strictly followed :\nRule 1 : provide genuine solutions to their problems \nRule 2 : Be their emotional friend support them emotionally\nRule 3 : Always provide solutions that make them emotionally strong.\nRule 4 : Provide them remedies to be emotionally strong.
\nRule 5 : If  user sounds too serious then recommend them to consult doctor immediately.
\n Rule 6 : Treat them like they are you close family member and support them.
\n Rule 7 : Ask them min 5 questions to understand their situation 
\n Rule 8 : Be Realistic with your answers in chat
\n Rule 9 : Don't repeat yourself in chat
\n Rule 10 : Make them feel safe and relax by talking to you
\n Rule 11 : Talk to them in a conversational manner like you are chatting with them
\n\n"
"""

@bot()
def on_message(message_history: List[Message], state: dict = None):

    # Generate GPT-3.5 Turbo response
    bot_response = OpenAI.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history, # Assuming history is the list of user messages
        model="gpt-3.5-turbo",
    )

    response = {
        "data": {
            "messages": [
                {
                    "data_type": "STRING",
                    "value": bot_response
                }
            ],
            "state": state
        },
        "errors": [
            {
                "message": ""
            }
        ]
    }

    return {
        "status_code": 200,
        "response": response
    }