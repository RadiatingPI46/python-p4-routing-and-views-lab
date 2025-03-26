#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:word>')
def print_string(word):
    print(word)
    return word

@app.route('/count/<int:integer>')
def count(integer):
    count = f''
    for n in range(integer):
        count += f'{n}\n'
    return count

@app.route('/math/<num1>/<operator>/<num2>')
def math(num1,operator,num2):
    if operator == '+':
        return str(int(num1) + int(num2))
    elif operator == '-':
        return str(int(num1) - int(num2))
    elif operator == '*':
        return str(int(num1) * int(num2))
    elif operator == 'div':
        return str(int(num1) / int(num2))
    elif operator == '%':
        return str(int(num1) % int(num2))
    else:
        return 'Invalid operator'
