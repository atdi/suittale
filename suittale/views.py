#!/usr/bin/env python
from . import app
from flask.templating import render_template


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/msuites")
def man_suites():
    return render_template('mensuits.html')


@app.route("/suitmeasures")
def suit_measures():
    return render_template('suit-measures.html',
                           table_html='guide/suit.html',
                           template_name='_suitMeasuresList.tmpl.html')


@app.route("/pantsmeasures")
def pants_measures():
    return render_template('suit-measures.html',
                           table_html='guide/pants.html',
                           template_name='_pantsMeasureList.tmpl.html')