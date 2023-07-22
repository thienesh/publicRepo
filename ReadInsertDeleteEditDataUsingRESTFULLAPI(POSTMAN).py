from flask import Flask, request
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
        data = APIUserModel.query.filter_by(id=id).first()
        return jsonify({"id": data.id, "name": data.name, "email": data.email})
    except:
        return jsonify({"ERROR_message": "ID not Found !"})


# INSERT DATA USING RESTFULL API
@app.route('/write', methods=['POST'])
def write():
    name = request.get_json()['name']
    email = request.get_json()['email']
    api_user_model = APIUserModel(name=name, email=email)
    try:
        db.session.add(api_user_model)
        db.session.commit()
    except:
        db.session.rollback()
        db.session.flush()
    id = api_user_model.id
    data = APIUserModel.query.filter_by(id=id).first()
    return jsonify({"id": data.id, "name": data.name, "email": data.email})


# DELETE by ID
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        APIUserModel.query.filter_by(id=id).delete()
        db.session.commit()
        return displayall()
    except:
        return jsonify({"message": "ID deos not exist. Please Check !!"})


# EDIT the data using POSTMAN RESTFULL API
@app.route('/edit/<int:id>', methods=['PATCH'])
def update_by_id(id):
    name = request.get_json()['name']
    email = request.get_json()['email']
    try:
        api_user_model = APIUserModel.query.filter_by(id=id).first()
        api_user_model.name = name
        api_user_model.email = email
        db.session.commit()
    except:
        return jsonify({"message": "ID deos not exist. Please Check !!"})
        db.session.rollback()
        db.session.flush()

    id = api_user_model.id
    data = APIUserModel.query.filter_by(id=id).first()
    return jsonify({"id": data.id, "name": data.name, "email": data.email})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
