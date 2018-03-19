from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
english_bot.set_trainer(ChatterBotCorpusTrainer)
for files in os.listdir('/home/ubuntu/Documents/chattter/chatterbot-corpus/chatterbot_corpus/data/english/'):
    data = open('/home/ubuntu/Documents/chattter/chatterbot-corpus/chatterbot_corpus/data/english/','r').readline()
    english_bot.train("chatterbot.corpus.english")


#
#english_bot.train("chatterbot.corpus.english")



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))


if __name__ == "__main__":
    app.run()