#!/usr/bin/env python3

import setuptools

setuptools.setup(
    name="embroidermodder",
    version="2.0-alpha",
    description="embroidermodder",
    author="The Embroidermodder Team",
    author_email="embroidermodder@gmail.com",
    entry_points={
        'console_scripts': ['embroidermodder=embroidermodder:new_file']
    },
    packages=setuptools.find_packages(include=['embroidermodder']),
    install_requires=[
        'libembroidery>=1.0a0'
    ],
    python_requires=">=3.6"
)
