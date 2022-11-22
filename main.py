from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def say_bye():
    return "<p>Bye</p>"

@app.route("/username/<path:name>/<int:number>")
def greet(name,number):
    return f"Hello there, {name}! You are {number} years old. "

if __name__ == "__main__":
    app.run(debug=True)