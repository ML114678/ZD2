from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Witaj w moim API!"

@app.route('/mojastrona')
def moja_strona():
    return "To jest moja strona!"

@app.route('/hello')
def hello():
    name = request.args.get('name')
    if name:
        return f"Witaj, {name}!"
    else:
        return "Witaj!"

@app.route('/api/v1.0/predict')
def predict():
    num1_str = request.args.get('num1')
    num2_str = request.args.get('num2')

    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
    except (TypeError, ValueError):
        return jsonify({"error": "Podaj poprawne liczby jako parametry num1 i num2"}), 400

    prediction = 1 if (num1 + num2) > 5.8 else 0

    output = {
        "prediction": prediction,
        "features": {
            "num1": num1,
            "num2": num2
        }
    }
    return jsonify(output)

if __name__ == '__main__':
    app.run()
