#!/usr/bin/env python

from setuptools import setup
import sys

assert sys.version_info.major == 3 and sys.version_info.minor >= 6, \
    "Safety Gym is designed to work with Python 3.6 and greater. " \
    + "Please install it before proceeding."

setup(
    name='safety_gym',
    packages=['safety_gym'],
    install_requires=[
        'Cython==0.29.36',
        'gymnasium==0.29.1',
        'joblib~=0.14.0',
        'mujoco_py==2.1.2.14',
        'numpy==1.24.4',
        'xmltodict==0.13.0',
    ],
)
