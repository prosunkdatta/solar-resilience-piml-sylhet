"""
QX-01 setup.py — package installation for local development.
Install in editable mode: pip install -e .
"""

from setuptools import setup, find_packages

setup(
    name='qx01-piml-solar-sylhet',
    version='0.1.0',
    author='Prosun Datta',
    author_email='prosunkdatta@gmail.com',
    description='Physics-Informed ML for Solar Microgrid Resilience — Sylhet',
    packages=find_packages(),
    python_requires='>=3.10',
)
