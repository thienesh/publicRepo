from flask import Flask, session

app = Flask(__name__)

app.config['SECRET_KEY'] = 'i_love_india'


# CREATE A SESSION
@app.route('/')
def index():
    if 'hits' in session:
        session['hits'] = session.get('hits') + 1
    else:
        session['hits'] = 1
    return 'Total no. of hits on the Application # {}'.format(session.get('hits'))


# DESTROY THE SESSION
@app.route('/delete')
def delete():
    session.pop('hits', None)
    return "Session Deleted successfully!!"


if __name__ == '__main__':
    app.run(debug=True, port=5000)
