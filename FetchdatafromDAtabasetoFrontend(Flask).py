from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote

app = Flask(__name__)

password = 'Thienesh8@'
encoded_password = quote(password)

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:{encoded_password}@localhost/thienesh'
app.config['SECRET_KEY'] = 'i_love_pizza'

db = SQLAlchemy(app)


# CREATE A TABLE INSIDE DATABASE THIENESH
class APIUserModel(db.Model):
    __tablename__ = 'bangalore_lockdown'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    email = db.Column(db.String(30))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form = request.form
        name = form['name']
        email = form['email']
        api_user_model = APIUserModel(name=name, email=email)

        try:
            with app.app_context():
                db.session.add(api_user_model)
                db.session.commit()
            return redirect(url_for('index'))
        except:
            db.session.rollback()
            db.session.flush()

    # READ ALL THE DATA FROM MYSQL DATABASE USING FLASK Sqlalchemy

    data = APIUserModel.query.all()
    return render_template('write-new.html', data=data)


# DELETE DATA
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    APIUserModel.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)
