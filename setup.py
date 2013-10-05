import os
from setuptools import find_packages
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "luna",
    version = "0.0.1",
    author = "Martin Matusiak",
    author_email = "numerodix@gmail.com",
    description = ("A Lua interpreter"),
    license = "MIT",
    keywords = "lua interpreter",
    #url = "http://packages.python.org/an_example_pypi_project",
    scripts=[
        "bin/lua",
    ],
    packages=find_packages(exclude=['tests']),
    install_requires=read('requirements.txt'),
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        #"Topic :: Utilities",
        #"License :: OSI Approved :: BSD License",
    ],
)
