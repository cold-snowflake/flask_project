from flask import Flask, render_template, request
from utils import get_answer, answers, houses

app = Flask(__name__)

@app.route('/')
def show_user_profile():
    return render_template("game_one/main.html")


@app.route('/game_one', methods=['GET', 'POST'])
def game_one():
    if request.method == 'GET':
        return render_template('game_one/game_one.html')
    return render_template("game_one/answer.html", name = request.form.get('name').capitalize(),
                            answer = get_answer(answers))


@app.route('/game_two', methods= ['GET', 'POST'])
def game_two_enter_name():
    if request.method == 'GET':
        return render_template("game_two/game_two_enter.html")
    return render_template("game_two/quetion_one.html")

@app.route('/game_two/result')
def result_game_two():
    return render_template("game_two/result.html",result = get_answer(houses))
    