import setuptools

import setuptools
import os

readme_path = os.path.join("..", "README.md")
with open(readme_path, "r") as f:
    long_description = f.read()

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

