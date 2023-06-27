from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return ("This is the Thienesh's Flask Application!!")

@app.route('/about')
def about():
    return ("This is the about page of Thienesh")

if __name__ == '__main__':
    app.run(debug=True, port=5000)