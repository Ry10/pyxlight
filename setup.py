#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup  # , find_packages
import subprocess, sys

## Run make on XFOIL fortran files
the_Command = 'make gfortran'
sys.stdout.flush()
proc = subprocess.Popen( the_Command, shell=True)
return_code = proc.wait()

setup(
    name='pyXLIGHT.py',
    version='0.1.0',
    description='Python version of XFOIL for airfoils',
    author='MDOLAB',
    author_email='mdolab.edu',
    package_dir={'': 'python'},
    py_modules=['pyXLIGHT'],
    license='Apache License, Version 2.0',
    data_files = [('', ['python/pyxlight.so', 'python/pyxlight_cs.so'])],
    zip_safe=False
)
