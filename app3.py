from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form = request.form
        name = form['my_name']
        return render_template('Display.html', data=name)
    return render_template('thienesh.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
