import setuptools
import os

setuptools.setup(
    name="qulacs-test",
    version="0.1.0",
    package_dir={'' : 'python'},
    py_modules=['qulacstest'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        'z-quantum-core',
        'cmake',
        'gcc7',
        'qulacs'
    ]
)

