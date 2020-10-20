from flask import Flask, render_template, request
# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
import os
import time
import subprocess

app = Flask(__name__)
question1 = ''

cur_object = ''
cur_img = -1

#english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
#trainer = ChatterBotCorpusTrainer(english_bot)
#trainer.train("chatterbot.corpus.english")

@app.route("/")
def home():
    #return render_template("index.html")
    return render_template("index.html", question=question1)

@app.route("/get")
def get_bot_response():
    #p.stdin.write(b'test\n')
    userText = request.args.get('msg')
    read_buffer_clear()
    write_buffer(userText)
    time.sleep(1)
    ret_text = wait_n_read()
    if len(ret_text) == 1:
        return ret_text[0]
    else:
        return ' '.join(ret_text)#ret_text[2], ret_text[0], ret_text[1]

# def wait_n_read():
#     ret_text = ''
#     temp_ret = ''
#     while "A (Yes,No,N/A)" not in ret_text:
#         temp_ret = read_buffer()
#         if len(temp_ret) > 0:
#             ret_text += temp_ret
#     return ret_text

def wait_n_read():
    ret_text = ''
    while len(ret_text) == 0:
        ret_text = read_buffer()
    return ret_text.split('|')

def read_buffer(path='../guesswhat/readbuffer'):
    with open(path, 'r') as f:
        ret_text = '\n'.join(f.readlines())
    return ret_text

def write_buffer(write_text, path='../guesswhat/writebuffer'):
    with open(path, 'w') as f:
        f.write(write_text)

def read_buffer_clear(path='../guesswhat/readbuffer'):
    with open(path, 'w') as f:
        pass

if __name__ == "__main__": 
    #p = subprocess.Popen(['python3', 'helloworld.py'], close_fds=True, stdin=subprocess.PIPE)
    question1 = wait_n_read() 
    app.run(host='0.0.0.0')
