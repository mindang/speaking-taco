import pygame
import torch
import tkinter
from stt import sst_function
import record
from test1 import test1aa
from test2 import test2aa
from pychatgpt import Chat, Options
import re

def talk():
    with torch.no_grad():
        record.stop()
        q = sst_function()
        label1['text'] = "나 : " + q
        answer_sentence = model.ask(q)
        label2['text'] = "타코 : " + answer_sentence
        print(answer_sentence)
        if len(answer_sentence)>=50:
            answer_sentence = answer_sentence[:50]
        answer_sentence = re.sub(r"[^ㄱ-ㅣ가-힣\s]", "", answer_sentence)
        test1aa(("".join(answer_sentence)))
        test2aa()
        pygame.mixer.init()
        answer_audio=pygame.mixer.Sound('output/0.wav')
        answer_audio.play()


options = Options()

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
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)

window = tkinter.Tk()
window.geometry("2000x1000")
window.resizable(1,1)
label1 = tkinter.Label(window,text='나 : ',font=('',50))
label1.place(x=0,y=0)
label2 = tkinter.Label(window,text='타코 : ',font=('',20),wraplength = 700)
label2.place(x=0,y=10)
button1 = tkinter.Button(window, text='녹음',command=record.start,font=('',35))
button2 = tkinter.Button(window, text='말걸기',command=talk,font=('',35))
button1.pack()
button2.pack()
label1.pack()
label2.pack()
window.mainloop()




