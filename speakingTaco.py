import pygame


import torch
from transformers import PreTrainedTokenizerFast, GPT2LMHeadModel
import tkinter

from stt import sst_function
import record
from test1 import test1aa
from test2 import test2aa

def talk():
    with torch.no_grad():
        #while 1:
        record.stop()
        q = sst_function()
        label1['text'] = "나 : " + q
        #q = input("user > ").strip()
        #if q == "quit":
            #break
        a = ""
        while 1:
            input_ids = torch.LongTensor(koGPT2_TOKENIZER.encode(Q_TKN + q + SENT + A_TKN + a)).unsqueeze(dim=0).to(device)
            pred = model(input_ids)
            pred = pred.logits#활성화 함수
            gen = koGPT2_TOKENIZER.convert_ids_to_tokens(torch.argmax(pred, dim=-1).squeeze().cpu().numpy().tolist())[-1]
            #gen = koGPT2_TOKENIZER.convert_ids_to_tokens(torch.argmax(pred, dim=-1).squeeze().numpy().tolist())[-1]

            if gen == EOS:
                break
            a += gen.replace("▁", " ")
        answer_sentence = ""
        for v in a.strip():
            answer_sentence += v

        label2['text'] = "타코 : " + answer_sentence
        print(answer_sentence)

        test1aa(("".join(answer_sentence)))
        test2aa()
        pygame.mixer.init()
        answer_audio=pygame.mixer.Sound('output/0.wav')
        answer_audio.play()


Q_TKN = "<usr>"
A_TKN = "<sys>"
BOS = '</s>'
EOS = '</s>'
MASK = '<unused0>'
SENT = '<unused1>'
PAD = '<pad>'

koGPT2_TOKENIZER = PreTrainedTokenizerFast.from_pretrained("skt/kogpt2-base-v2",
            bos_token=BOS, eos_token=EOS, unk_token='<unk>',
            pad_token=PAD, mask_token=MASK)
model = GPT2LMHeadModel.from_pretrained('simsim.pt')
#model = GPT2LMHeadModel.from_pretrained('skt/kogpt2-base-v2')
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
#device = torch.device("cpu")
model.to(device)
print(device)


window = tkinter.Tk()
window.geometry("2000x1000")
window.resizable(1,1)
label1 = tkinter.Label(window,text='나 : ',font=('',50))
label1.place(x=0,y=0)
label2 = tkinter.Label(window,text='타코 : ',font=('',50),wraplength = 700)
label2.place(x=0,y=10)
button1 = tkinter.Button(window, text='녹음',command=record.start,font=('',35))
button2 = tkinter.Button(window, text='말걸기',command=talk,font=('',35))
button1.pack()
button2.pack()
label1.pack()
label2.pack()
window.mainloop()




