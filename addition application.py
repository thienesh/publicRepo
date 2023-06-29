from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('inout.html')

@app.route('/compute', methods=['POST'])
def compute():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    result = num1 + num2
    print(f"{num1} and {num2} addition is {result}")

    return jsonify({'result': result})

if __name__ == '__main__':
    #app.run()
    app.run(debug=True,port=5000)