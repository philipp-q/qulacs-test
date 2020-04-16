import setuptools
import os

setuptools.setup(
    name="qulacs-test",
    version="0.1.0",
    py_modules=['qulacstest'],
    install_requires=[
        'cmake',
        'gcc7',
        'qulacs'
    ]
)

