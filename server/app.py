#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
    
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<text>')
def print_text(text):
    print(text)
    return text

@app.route('/count/<int:number>')
def count(number):
    count = ''
    for i in range(number):
        count += str(i) + '\n'
    return count

@app.route('/math/<int:number1>/<operation>/<int:number2>')
def math(number1, operation, number2):
    if operation == '+':
        return str(number1 + number2)
    elif operation == '-':
        return str(number1 - number2)
    elif operation == '*':
        return str(number1 * number2)
    elif operation == 'div':
        return str(number1 / number2)
    elif operation == '%':
        return str(number1 % number2)
    else:
        return 'Invalid operation'
    
