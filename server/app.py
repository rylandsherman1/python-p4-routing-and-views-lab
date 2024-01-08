#!/usr/bin/env python3
from flask import Flask, escape

app = Flask(__name__)


# Index view
@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


# Print string view
@app.route("/print/<string:text>")
def print_string(text):
    print(text)  # This will print the string to the terminal
    return escape(text)  # Display the string in the web browser


# Count view
@app.route("/count/<int:num>")
def count(num):
    # Join the numbers from 0 to num-1 with newline, and add a trailing newline
    return "\n".join(str(i) for i in range(num)) + "\n"


# Math operation view
@app.route("/math/<int:num1>/<string:operation>/<int:num2>")
def math(num1, operation, num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    elif operation == "%":
        result = num1 % num2
    else:
        return "Invalid operation"

    return str(result)


if __name__ == "__main__":
    app.run(port=5555, debug=True)
