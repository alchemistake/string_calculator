from flask import Flask, Response, request, jsonify

from backend.calculator import Calculator

app = Flask(__name__)
calculator = Calculator()


@app.route('/calc', methods=["POST"])
def calc():
    data = request.json
    if data:
        try:
            result = calculator.calculate(data["expression"])
            return jsonify({"result": result}), 200
        except (ArithmeticError, ValueError, TypeError):
            Response("You should send JSON format and valid arithmetic expression", 400)
    return Response("You should send JSON data with the POST request", 400)


if __name__ == '__main__':
    app.run()
