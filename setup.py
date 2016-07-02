"""
prettyqr

https://github.com/olorin/prettyqr
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    desc = f.read()

setup(
    name="prettyqr",
    version="0.0.1",
    description="Create QR codes merged with images.",
    long_description=desc,
    url="https://github.com/olorin/prettyqr",
    author="Sharif Olorin",
    author_email="sio@tesser.org",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Graphics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
    keywords="qrcode image",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "pillow>=3.2",
        "qrcode>=5.3",
    ],
    entry_points={
        "console_scripts": [
            "prettyqr=prettyqr.cli:main",
        ],
    },
)
