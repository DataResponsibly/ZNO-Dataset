import os
from setuptools import setup, find_packages


with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name='ZNODataset',
    version='0.0.1',
    author='Nazarii Drushchak, Tetiana Herasymova, Olha Liuba, Sandra Konopatska, Andrew Bell, Julia Stoyanovich',
    author_email='naz2001r@gmail.com',
    description='ZNO benchmarks',
    install_requires=required,
    python_requires='>=3.7',
    packages=find_packages()
)