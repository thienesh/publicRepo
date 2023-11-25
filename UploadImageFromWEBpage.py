from flask import Flask, render_template, redirect, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'C:/Users/Admin/PycharmProjects/publicRepo/static/img'
app.config['SECRET_KEY'] = 'I_love_pizza'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect('/')
        file = request.files['file']
        if file.filename == '':
            return "<script> alert('File not found !')</script>"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect('/')
        else:
            return redirect(request.url)
    return render_template('uploadimage.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
