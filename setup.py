#!/bin/python
from setuptools import setup
setup(
    name='protozfitsreader',
    packages=['protozfitsreader'],
    version='0.41',
    description='Basic python bindings for protobuf zfits reader',
    author="Etienne Lyard et al.",
    author_email="etienne.lyard@unige.ch",
    package_data={'': ['*.so*']},
    install_requires=['numpy', 'protobuf'],
)
