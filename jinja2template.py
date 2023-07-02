from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    name = "Thienesh Raaj"
    return render_template('upload.html', data=name)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
