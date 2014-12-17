#!/usr/bin/env python
from . import app
from flask.templating import render_template


@app.route("/")
def hello():
    return render_template('index.html')