#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers=[str(i) for i in range(parameter)]
    return '\n'.join(numbers) + '\n'

@app.route("/math/<int:num1>/<op>/<int:num2>")
def math(num1, op, num2):
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "div":
        result = num1 / num2 if num2 != 0 else "undefined"
    elif op == "%":
        result = num1 % num2 if num2 != 0 else "undefined"
    else:
        return "Invalid operation"

    return str(result)
