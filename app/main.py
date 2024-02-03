from flask import Flask, render_template, request
from utils import get_answer, answers

app = Flask(__name__)

@app.route('/')
def show_user_profile():
    return render_template("main.html")


@app.route('/game_one', methods=['GET', 'POST'])
def game_one():
    if request.method == 'GET':
        return render_template('game_one.html')
    return render_template("answer.html", name = request.form.get('name').capitalize(),
                            answer = get_answer(answers))

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f'Subpath {escape(subpath)}'

# with app.test_request_context():
#     print(url_for('show_user_profile'))
#     print(url_for('show_post'))
    # print(url_for('login', next='/'))
    # print(url_for('profile', username='John Doe'))