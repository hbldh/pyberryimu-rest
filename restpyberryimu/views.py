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

import os
import uuid
import datetime
import json

from flask import render_template, jsonify, request, redirect, send_file
from concurrent.futures import ThreadPoolExecutor

from restpyberryimu import app, forms, config


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
            return redirect('/new_session_failed', code=307)
    return render_template('new_session.html',
                           title='New Session Page',
                           form=new_session_form)


@app.route('/new_session_started', methods=['POST'])
def new_session_started():
    new_session_form = forms.NewSessionForm()
    this_uuid = uuid.uuid4()
    filepath_to_save_to = os.path.join(config.SAVE_FOLDER, str(this_uuid) + '.json')
    settings = _parse_settings(new_session_form)
    settings['uuid'] = this_uuid

    def function_to_call(savefile_path, settings_dict):
        try:
            from pyberryimu.client import BerryIMUClient
            from pyberryimu.calibration.standard import StandardCalibration
            from pyberryimu.recorder import BerryIMURecorder
            with BerryIMUClient(settings=settings_dict) as c:
                c.calibration_object = StandardCalibration.load()
                r = BerryIMURecorder(c, settings_dict.get('data_rate'),
                                     settings_dict.get('duration'))
                out = r.record()
            out.save(savefile_path)
        except Exception as e:
            with open(savefile_path, 'wt') as f:
                json.dump({'error': str(e)}, f, indent=2)
    with ThreadPoolExecutor(max_workers=1) as ex:
        future = ex.submit(function_to_call, filepath_to_save_to, settings)
    return render_template('new_session_started.html',
                           title='New Session Started',
                           settings=settings)


@app.route('/new_session_failed', methods=['POST'])
def new_session_failed():
    return jsonify(**dict(request.form))


@app.route('/past_sessions', methods=['GET'])
def past_sessions():
    stored_files = []
    for pth, dirs, files in os.walk(config.SAVE_FOLDER):
        for f in files:
            with open(os.path.join(pth, f)) as fp:
                doc = json.load(fp)
            if 'error' in doc:
                stored_files.append({'name': 'ERROR: {0}'.format(doc.get('error')),
                                     'date': datetime.datetime.now(),
                                     'uuid':  os.path.splitext(f)[0]})
            else:
                stored_files.append({'name': doc.get('name'),
                                     'date': doc.get('recorded'),
                                     'uuid': os.path.splitext(f)[0]})
    return render_template('past_sessions.html',
                           title='Past Sessions Page',
                           files=stored_files)


@app.route('/item_page/<this_uuid>', methods=['GET'])
def item_page(this_uuid):
    return send_file(os.path.join(config.SAVE_FOLDER, this_uuid + ".json"),
                     mimetype='application/json')


def _parse_settings(nfs):
    return {
        'name': nfs.name.data,
        'data_rate': int(nfs.data_rate.data),
        'duration': int(nfs.duration.data),
        'accelerometer': {
            'data_rate': float(nfs.acc_data_rate.data),
            'continuous_update': nfs.acc_continuous_update.data,
            'enabled_x': nfs.acc_enabled_x.data,
            'enabled_y': nfs.acc_enabled_y.data,
            'enabled_z': nfs.acc_enabled_z.data,
            'anti-alias': int(nfs.acc_antialias.data),
            'full_scale': int(nfs.acc_fullscale.data),
            'self_test': int(nfs.acc_selftest.data) if nfs.acc_selftest.data != 'X' else 'X'
        },
        'gyroscope': {
            'data_rate': int(nfs.gyro_data_rate.data),
            'bandwidth_level': int(nfs.gyro_bandwidth_level.data),
            'powerdown_mode': nfs.gyro_powerdown_mode.data,
            'enabled_z': nfs.gyro_enabled_z.data,
            'enabled_y': nfs.gyro_enabled_y.data,
            'enabled_x': nfs.gyro_enabled_x.data,
            'continuous_update': nfs.gyro_continuous_update.data,
            'little_endian': nfs.gyro_little_endian.data,
            'full_scale': int(nfs.gyro_fullscale.data),
            'self_test': int(nfs.gyro_selftest.data)
        },
        'magnetometer': {
            'enabled_temp': True,
            'data_rate': float(nfs.mag_data_rate.data),
            'full_scale': int(nfs.mag_fullscale.data),
            'sensor_mode': int(nfs.mag_sensor_mode.data),
            'lowpower_mode': False,
            'high_resolution': True
        }
    }
