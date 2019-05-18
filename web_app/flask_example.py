from flask import Flask, render_template, request
from modules.process_match import process_match

app = Flask(__name__)


@app.route("/")
def start(name1=None, name2=None):

    return render_template("index.html", name1=name1, name2=name2, type=type)


@app.route("/results", methods=["POST"])
def results():
    player1 = str(request.form.get("name1"))
    player2 = str(request.form.get("name2"))
    type = str(request.form.get("type"))
    gender = str(request.form.get("gender"))
    chance = process_match(player1, player2, type, gender)
    return render_template("results.html", player1=player1, player2=player2, type=type, gender=gender, chance=chance)


if __name__ == "__main__":
    app.run()
