from flask import Flask, render_template
from words import BeeWords

app = Flask(__name__)
my_bee = BeeWords("words.txt")


@app.route('/random-word')
def random_word():
    return my_bee.get_word()


@app.route('/')
def index():
    word = my_bee.get_word()
    return render_template('index.html', word_est=word["estonian"], word_eng=word["english"])


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
