#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:mod:`views.py`
==================

.. module:: views.py
   :platform: Unix, Windows
   :synopsis:

.. moduleauthor:: hbldh <henrik.blidh@swedwise.com>

Created on 2014-09-09, 15:08

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import uuid
import datetime
import numpy as np

from flask import render_template, jsonify, request, redirect, make_response

from restpyberryimu import app, forms



@app.route('/', methods=['GET', ])
def index():
    return render_template('index.html',
                           title='Home')

@app.route('/new_session', methods=['GET', 'POST'])
def new_session():
    new_session_form = forms.NewSessionForm()
    if request.method == 'POST':
        if new_session_form.validate_on_submit():
            return redirect('/new_session_started', code=307)
        else:
            return redirect('/new_session_failed')
    return render_template('new_session.html',
                           title='New Session Page',
                           form=new_session_form)


@app.route('/new_session_started', methods=['POST'])
def new_session_started():
    this_uuid = uuid.uuid4()
    settings = dict(request.form)
    settings['uuid'] = this_uuid
    return jsonify(**settings)


@app.route('/new_session_failed', methods=['GET'])
def new_session_failed():
    return jsonify(**request.form)


@app.route('/past_sessions', methods=['GET'])
def past_sessions():
    return render_template('past_sessions.html',
                           title='Past Sessions Page')


