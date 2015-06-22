#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:mod:`filters.py`
==================

.. module:: filters.py
   :platform: Unix, Windows
   :synopsis:

.. moduleauthor:: hbldh <henrik.blidh@nedomkull.com>

Created on 2015-06-22, 21:58

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

from restpyberryimu import app


@app.template_filter('sort_keys')
def sort_keys(obj):
    return sorted(obj.keys())


@app.template_filter('swedate')
def swedate(s):
    return s.strftime("%Y-%m-%d %H:%M:%S")

