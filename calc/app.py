from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route('/add?<int:a>&<int:b>')
def add():
    a = request.args["a"]
    b = request.args["b"]
    return add(a, b)

@app.route('/sub?<int:a>&<int:b>')
def sub():
    a = request.args["a"]
    b = request.args["b"]
    return sub(a, b)

@app.route('/mult?<int:a>&<int:b>')
def mult():
    a = request.args["a"]
    b = request.args["b"]
    return mult(a, b)

@app.route('/div?<int:a>&<int:b>')
def div():
    a = request.args["a"]
    b = request.args["b"]
    return div(a, b)