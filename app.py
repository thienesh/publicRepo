from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "This is the 'Thinness's' Flask Application!!"


@app.route('/about')
def about():
    return "You have just arrived at About page!!"


if __name__ == '__main__':
    app.run(debug=True, port=5000)
