#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)


@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string:parameter>")
def print_string(parameter):
    print(f"{parameter}")
    return f"{parameter}"

@app.route("/count/<int:parameter>")
def count(parameter):
    numbers = ""
    for i in range(parameter):
        numbers += f"{i}\n"
    return numbers

@app.route("/math/<float:num1>/<operation>/<float:num2>")
def math(num1, num2, operation):
    
    if operation == "+":
        return  str(num1 + num2)

    elif operation == "-":
        return str(num1 - num2)

    elif operation == "*":
        return  str(num1 * num2)

    elif operation == "div":
        if num2 != 0:
              return str(num1 / num2)
        else:
            return "Cannot divide by 0"
        
    elif operation == "%":
          return str(num1 % num2)
    else:
        return "Please enter a valid operation"

    