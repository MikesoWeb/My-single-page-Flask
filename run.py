from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap5 = Bootstrap5(app)


@app.route('/')
def index():
    title = 'Мой одностраничник'
    return render_template('index.html', title=title)


if __name__ == '__main__':
    app.run(debug=True, port=5666)
