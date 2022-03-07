from __future__ import print_function, division, unicode_literals
import json

from flask import Flask,request, render_template, jsonify
import emoji


from torchmoji.sentence_tokenizer import SentenceTokenizer
from torchmoji.model_def import torchmoji_emojis
from torchmoji.global_variables import PRETRAINED_PATH, VOCAB_PATH


# Initalise the Flask app
app = Flask(__name__)


# Emoji map in emoji_overview.png
EMOJIS = ":joy: :unamused: :weary: :sob: :heart_eyes: \
:pensive: :ok_hand: :blush: :heart: :smirk: \
:grin: :notes: :flushed: :100: :sleeping: \
:relieved: :relaxed: :raised_hands: :two_hearts: :expressionless: \
:sweat_smile: :pray: :confused: :kissing_heart: :heartbeat: \
:neutral_face: :information_desk_person: :disappointed: :see_no_evil: :tired_face: \
:v: :sunglasses: :rage: :thumbsup: :cry: \
:sleepy: :yum: :triumph: :hand: :mask: \
:clap: :eyes: :gun: :persevere: :smiling_imp: \
:sweat: :broken_heart: :yellow_heart: :musical_note: :speak_no_evil: \
:wink: :skull: :confounded: :smile: :stuck_out_tongue_winking_eye: \
:angry: :no_good: :muscle: :facepunch: :purple_heart: \
:sparkling_heart: :blue_heart: :grimacing: :sparkles:".split(' ')

MAX_LEN = 500
VOCABULARY = None
MODEL = None
ST = None

def top_elements(array, k):
    ind = np.argpartition(array, -k)[-k:]
    return ind[np.argsort(array[ind])][::-1]

@app.route('/')
def home():
    return render_template("home.html")

# @app.route('/emojize',methods=['GET'])
# def emojize():
#     text = str(request.args.get('text'))
#     tokenized, _, _ = ST.tokenize_sentences([text])
#     prob = MODEL(tokenized)[0]

#     emoji_ids = top_elements(prob, 10)

#     emojis = map(lambda x: EMOJIS[x], emoji_ids)
#     emolist = list(emojis)
#     return " ".join([emoji.emojize(x, use_aliases=True) for x in emolist ])

if __name__ == '__main__':
    # with open(VOCAB_PATH, 'r') as f:
    #     VOCABULARY = json.load(f)

    # ST = SentenceTokenizer(VOCABULARY, MAX_LEN)
    # MODEL = torchmoji_emojis(PRETRAINED_PATH)

    app.run(debug=True)