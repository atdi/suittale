#!/usr/bin/env python
from . import app
from flask.templating import render_template


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')