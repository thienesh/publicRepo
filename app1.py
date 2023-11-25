from flask import Flask

app = Flask(__name__)

#Simple routing
@app.route('/')
def index():
    return ("This is the Thienesh's Flask Application!!")

#Another example of simple route
@app.route('/about')
def about():
    return ("This is the about page of Thienesh")

#Vanity URL Dynamic URL
@app.route('/about/<name>')
def author(name):
    return ('The name of the author is ' + name)

#VANITY URL 2
@app.route('/author/<name>/<subject>')
def author_with_sub(name, subject):
    return ('The name of the author is '+ name + " .And he reads "+ subject )

if __name__ == '__main__':
    app.run(debug=True, port=5000)