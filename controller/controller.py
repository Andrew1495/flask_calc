from flask import render_template
from app import app
from models.calculator import *

@app.route('/<int:num1>/<operator>/<int:num2>')

def index(num1, operator, num2):
    if operator == "+":
        total = add(num1, num2)
        return render_template("index.html", total=total)
    
    elif operator == '-':
        total = sub(num1, num2)
        return render_template("index.html", total=total)

    elif operator == '*':
        total = multiply(num1, num2)
        return render_template("index.html", total=total)

    elif operator == '/':
        total = divide(num1, num2)
        return render_template("index.html", total=total)



