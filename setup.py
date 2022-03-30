#!/usr/bin/env python3

import setuptools

setuptools.setup(
    name="embroidermodder",
    version="2.0-alpha-4",
    url="https://embroidermodder.org",
    description="embroidermodder",
    license="zlib",
    author="The Embroidermodder Team",
    author_email="embroidermodder@gmail.com",
    entry_points={
        'console_scripts': ['embroidermodder=embroidermodder:main']
    },
    packages=setuptools.find_packages(include=['embroidermodder']),
    install_requires=[
        'libembroidery>=1.0a0'
    ],
    include_package_data=True,
    python_requires=">=3.7",
    test_suite='test',
    build_apps={
        "gui_apps": {
            "Embroidermodder 2": "embroidermodder/__main__.py"
        },
        "icons": {
            "Embroidermodder 2": ["embroidermodder2.ico"]
        }
    }
)
