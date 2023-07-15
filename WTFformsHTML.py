from flask import Flask, render_template, request
from flask_wtf import Form
from wtforms.fields import TextAreaField, PasswordField, SubmitField


app = Flask(__name__)
app.config['SECRET_KEY'] = 'i_love_pizza'

class UserForm(Form):
    username = TextAreaField("Name of the User: ")
    password = PasswordField("User Password: ")
    submit = SubmitField("ENTER CREDENTIALS")

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = UserForm()
    if request == 'POST':
        return render_template('Display.html')
    return render_template('uploadWTF.html', form=form)



if __name__ == '__main__':
    app.run(debug=True, port=5000)
