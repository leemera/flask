from flask import Flask, render_template

app = Flask(__name__)

users = [
    {"id": 1, "name": "김오즈", "email": "ozcoding@naver.com"},
    {"id": 2, "name": "김철수", "email": "kim@naver.com"},
    {"id": 3, "name": "유한성", "email": "you@naver.com"},
    {"id": 4, "name": "이한별", "email": "lee@naver.com"},
    {"id": 5, "name": "윤설", "email": "yoon@naver.com"}
]

@app.route('/')
def user_list():
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)