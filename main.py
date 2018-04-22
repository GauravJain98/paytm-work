from flask import Flask, request, render_template

app = Flask(__name__)

# @ signifies a decorator - way to wrap a function and modifying its behavior
@app.route('/')
def index():
    return render_template("profile.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)