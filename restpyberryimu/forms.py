#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:mod:`forms`
==================

.. module:: forms
   :platform: Unix, Windows
   :synopsis: 

.. moduleauthor:: hbldh <henrik.blidh@nedomkull.com>

Created on 2015-06-29, 22:39

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

from flask_wtf import Form
from wtforms import StringField, SelectField, IntegerField, BooleanField
from wtforms.validators import DataRequired


class NewSessionForm(Form):
    name = StringField('Recording Name', validators=[DataRequired()])
    data_rate = SelectField('Data Rate', choices=[
        ("50", '50 Hz'), ("100", '100 Hz'), ("150", '150 Hz'), ("200", '200 Hz')],
                            validators=[DataRequired()], default="200")
    duration = IntegerField('Recording Duration', validators=[DataRequired(), ])

    acc_data_rate = SelectField('Data Rate', choices=[
        ("0", '0 Hz'), ("3.125", '3.125 Hz'), ("6.25", '6.25 Hz'), ("12.5", '12.5 Hz'),
        ("25", '25 Hz'), ("50", '50 Hz'), ("100", '100 Hz'), ("200", '200 Hz'),
        ("400", '400 Hz'), ("800", '800 Hz'), ("1600", '1600 Hz'), ], default="200")
    acc_continuous_update = BooleanField("Continuous Update", default=False)
    acc_enabled_x = BooleanField("Enabled X-axis sensor", default=True)
    acc_enabled_y = BooleanField("Enabled Y-axis sensor", default=True)
    acc_enabled_z = BooleanField("Enabled Z-axis sensor", default=True)

    acc_antialias = SelectField('Anti-alias filter bandwidth', choices=[
        ("773", '773 Hz'), ("194", '194 Hz'), ("362", '362 Hz'), ("50", '50 Hz'), ], default="773")
    acc_fullscale = SelectField('Full scale', choices=[
        ("2", '2 g'), ("4", '4 g'), ("6", '6 g'), ("8", '8 g'),
        ("16", '16 g'), ], default="8")
    acc_selftest = SelectField('Self-test', choices=[
        ("0", 'Normal mode'), ("1", 'Positive sign self-test'),
        ("-1", 'Negative sign self-test'), ('X', 'Not allowed'), ], default="0")

    gyro_data_rate = SelectField('Data Rate', choices=[
        ("95", '95 Hz'), ("190", '190 Hz'), ("380", '380 Hz'), ("760", '760 Hz'), ], default="190")
    gyro_bandwidth_level = SelectField('Bandwidth Level', choices=[
        ("0", '0'), ("1", '1'), ("2", '2'), ("3", '3'), ], default=0)
    gyro_continuous_update = BooleanField("Continuous Update", default=False)
    gyro_little_endian = BooleanField("Little Endian", default=False)
    gyro_powerdown_mode = BooleanField("Power-Down mode", default=False)
    gyro_enabled_x = BooleanField("Enabled X-axis sensor", default=True)
    gyro_enabled_y = BooleanField("Enabled Y-axis sensor", default=True)
    gyro_enabled_z = BooleanField("Enabled Z-axis sensor", default=True)
    gyro_fullscale = SelectField('Full scale', choices=[
        ("245", '245 deg/s'), ("500", '500 deg/s'), ("2000", '2000 deg/s'), ], default="500")
    gyro_selftest = SelectField('Self-test', choices=[
        ("0", 'Normal mode'), ("1", 'Positive sign self-test'),
        ("-1", 'Negative sign self-test'), ], default="0")

    mag_data_rate = SelectField('Data Rate', choices=[
        ("0", '0 Hz'), ("3.125", '3.125 Hz'), ("6.25", '6.25 Hz'), ("12.5", '12.5 Hz'),
        ("25", '25 Hz'), ("50", '50 Hz'), ("100", '100 Hz'), ], default="50")
    mag_fullscale = SelectField('Full scale', choices=[
        ("2", '2 gauss'), ("4", '4 gauss'), ("8", '8 gauss'), ("12", '12 gauss')], default="12")
    mag_sensor_mode = SelectField('Sensor Mode', choices=[
        ("0", 'Continuous-conversion mode'),
        ("1", 'Single-conversion mode'),
        ("-1", 'Power-down mode'), ], default="0")
