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

import datetime
import numpy as np

from flask import render_template, jsonify, request, redirect, make_response
from restpyberryimu import app

@app.route('/', methods=['GET', ])
def index():
    return render_template('index.html',
                           title='Home')

@app.route('/new_session', methods=['GET', 'POST'])
def new_session():
    return render_template('index.html',
                           title='New Session Page')

@app.route('/past_sessions', methods=['GET'])
def past_sessions():
    return render_template('index.html',
                           title='Past Sessions Page')

