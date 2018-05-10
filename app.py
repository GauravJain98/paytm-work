from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("about.html")

@app.route('/privacy')
def privacy():
    return render_template("privacy.html")

@app.route('/refund')
def refund():
    return render_template("refund.html")

@app.route('/terms')
def terms():
    return render_template("terms.html")

@app.route('/contact')
def contact_us():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)
