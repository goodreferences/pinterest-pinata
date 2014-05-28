#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name="pinterest-pinata",
      version="0.1.0",
      description="Pinterest client",
      install_requires=["requests==0.13.9"],
      author="Alexi Rahman",
      author_email="alexi.rahman@r76.se",
      url="http://github.com/odynvolk/pinterest-pinata",
      packages=find_packages(),
      keywords="pinterest api",
      zip_safe=True)

