from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

@app.route('/box')
def box():
    return (render_template('box.html'))

@app.route('/brain')
def brain():
    return (render_template('brain.html'))
