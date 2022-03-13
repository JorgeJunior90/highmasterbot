from pyexpat.errors import messages
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

class MasterBot:
    def __init__(self):
        TOKEN = os.getenv("API_KEY")
        self.url = f"https://api.telegram.org/bot{TOKEN}/"

    def start(self):
        updateID = None 
        while True:
           update = self.get_message(updateID)
           messages = update['result']
           if messages:
               for message in messages:
                    try:
                       updateID = message['update_id']
                       chatID = message['message']['from']['id']
                       message_text = message['message']['text']
                       answer_bot =  self.create_answer(message_text)
                       self.send_answer(chatID, answer_bot)
                    except:
                        pass

    def get_message(self, updateID):
        link_request = f"{self.url}getUpdates?timeout=1000"
        if updateID:
            link_request = f"{self.url}getUpdates?timeout=1000&offset={updateID+1}"
        result =requests.get(link_request)
        return json.loads(result.content)

    def create_answer(self, message_text):
        return "Ola, Tudo Bem?"

    def send_answer(self, chatID, answer):
        link_to_send = f"{self.url}sendMessage?chat_id={chatID}&text={answer}"
        requests.get(link_to_send)
        return