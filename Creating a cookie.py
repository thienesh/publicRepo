from flask import Flask, render_template, request, make_response

app = Flask(__name__)


# CREATE A COOKIE
@app.route('/')
def index():
    cookie = make_response("Creating a cookie")
    cookie.set_cookie('name', 'thienesh', max_age=60 * 60)
    return (cookie)


# READ THE COOKIE
@app.route('/read')
def read_cookie():
    if request.cookies.get('name'):
        cookie = make_response("Display cookie : {}".format(request.cookies.get('name')))
    else:
        cookie = make_response("Creating a cookie")
    cookie.set_cookie('name', 'raaj', max_age=60 * 60)
    return (cookie)


if __name__ == '__main__':
    # app.run()
    app.run(debug=True, port=5000)
