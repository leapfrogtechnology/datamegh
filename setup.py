""" Package setup. """

import setuptools

import datamegh

# Requirements
requirements = ["pyodbc>=4.0.27,<5", "flatten_json==0.1.7"]

# Development Requirements
requirements_dev = ["pytest==4.*", "mock==3.0.5", "black==19.10b0"]

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name=datamegh.name,
    version=datamegh.version,
    description="Datamegh - Engineered for the cloud.",
    author="Kabir Baidhya",
    author_email="kabirbaidhya@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leapfrogtechnology/datamegh",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    extras_require={"dev": requirements_dev},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
