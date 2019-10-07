from flask import Flask, render_template, request, send_file
from words import BeeWords
import io

app = Flask(__name__)
my_bee = BeeWords("words.txt")


@app.route('/random-word', methods=["GET"])
def random_word():
    w = my_bee.get_word()
    return w


@app.route('/update', methods=["POST"])
def update_stats():
    if request.method == "POST":
        pass
        # print(dict(request.json))

    w = my_bee.get_word()
    return w


@app.route('/polly')
def polly():
    w = request.args.get('w')
    if w is not None:
        a = my_bee.say_english(w)
        return send_file(io.BytesIO(a),
                         attachment_filename=w+'.mp3',
                         mimetype='audio/mp3')


@app.route('/')
def index():
    w = my_bee.get_word()
    a = my_bee.say_english(w["english"])
    return render_template('index.html',
                           word_est=w["estonian"], word_eng=w["english"], audio=a)


if __name__ == '__main__':
    # app.run()

    while True:
        word = my_bee.get_word()
        print("Järgmine sõna eesti keeles: " + word["estonian"])
        answer = input("Inglise keeles on see: ")

        if answer == word["english"]:
            print("Tubli!")
        else:
            print("Proovi veel, õige vastus oli: " + word["english"] + " aga sina kirjutasid " + answer)
