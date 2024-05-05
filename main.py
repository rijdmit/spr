from flask import Flask, render_template, session, redirect, url_for


app = Flask(__name__)
app.secret_key = 'secret_key'

coins=100
showel_on = False

@app.route('/')
def index():
    return render_template('index.html', coins=coins, showel_on=showel_on)


app.run(debug=True)
