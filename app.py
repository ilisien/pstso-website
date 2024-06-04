from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("base.html")

@app.route('/join')
def join():
    return "This is the join page."

@app.route('/about')
def about():
    return "This is the about page."

@app.route('/faqs')
def faqs():
    return "This is the faqs page."

@app.route('/leadership')
def leadership():
    return "This is the leadership page."

@app.route('/support')
def support():
    return "This is the support page."

@app.route('/font-licenses')
def font_licenses():
    return "This is the font-licenses page."

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")