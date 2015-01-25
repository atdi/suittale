#!/usr/bin/env python
from . import app
from flask.templating import render_template


@app.route("/msuites")
def man_suites():
    return render_template('products-list.html')


@app.route("/suittextures")
def suit_textures():
    return render_template('textures-list.html')


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


@app.route("/coatsmeasures")
def coats_measures():
    return render_template('suit-measures.html',
                           table_html='guide/coats.html',
                           template_name='_coatsMeasureList.tmpl.html')