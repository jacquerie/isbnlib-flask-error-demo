#!/usr/bin/env python

# Comment me out for the example to work
from micawber.providers import Provider
p = Provider('')
p.fetch('http://www.google.com')

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<img src="/static/tux.png">'

if __name__ == '__main__':
    app.run(debug=True)
