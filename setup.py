#!/usr/bin/env python
# encoding: utf-8

import sys
import os
from setuptools import dist

try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension


if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

desc = open("README.rst").read()

# install numpy so we can import it before calling setup
# https://luminousmen.com/post/resolve-cython-and-numpy-dependencies
dist.Distribution().fetch_build_eggs(['numpy'])
import numpy
include_dirs = [
    "acor",
    numpy.get_include(),
]

acor = Extension("acor._acor", ["acor/_acor.c", "acor/acor.c"],
                 include_dirs=include_dirs)

setup(
    name="acor",
    version="1.1.1",
    author="Daniel Foreman-Mackey and Jonathan Goodman",
    author_email="danfm@nyu.edu",
    packages=["acor"],
    url="http://github.com/dfm/chimaerase",
    license="MIT",
    description="Estimate the autocorrelation time of a time series quickly.",
    long_description=desc,
    install_requires=["numpy"],
    ext_modules=[acor],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
)
