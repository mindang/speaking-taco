import pygame
import torch
import tkinter
from stt import sst_function
import record
from test1 import test1aa
from test2 import test2aa
from pychatgpt import Chat, Options
import re





options = Options()
options.log = True
# Track conversation
options.track = True

# Use a proxy
options.proxies = 'http://localhost:8080'

# Optionally, you can pass a file path to save the conversation
# They're created if they don't exist
options.chat_log = "chat_log.txt"
options.id_log = "id_log.txt"

# Create a Chat object
#chat = Chat(email="id", password="pw", conversation_id="Previous Conversation ID", previous_convo_id="Previous Conversation ID")
model = Chat(email="id", password="pw")
while 1:
    q = input("입력 : ").strip()
    q = re.sub(r"[^ㄱ-ㅣ가-힣\s]", "", q)
    print(model.ask(q))


