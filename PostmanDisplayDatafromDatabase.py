from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask import jsonify

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


# READ DATA USing RESTFULL API
@app.route('/displayall', methods=['GET'])
def displayall():
    data = APIUserModel.query.all()
    data_all = []
    for data in data:
        data_all.append({"id": data.id, "name": data.name, "email": data.email})
    return jsonify(data_all)


# Display using ID
@app.route('/display/<int:id>', methods=['GET'])
def display_by_id(id):
    try:
        data = APIUserModel.query.filter_by(id = id).first()
        return jsonify({"id": data.id, "name": data.name, "email": data.email})
    except:
        return jsonify({"ERROR_message": "ID not Found !"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
