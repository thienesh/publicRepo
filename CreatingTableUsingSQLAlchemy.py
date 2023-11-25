from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote

try:
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


    if __name__ == "__main__":
        db.create_all()
        app.run(debug=True, port=5000)

except Exception as e:
    print(e)
