#!/usr/bin/env python3
import os
from distutils.core import setup
import setuptools
# Build and push this package with: ./setup.py sdist bdist_wheel && twine upload dist/*

currentDir = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(currentDir, 'README.md'), encoding='utf-8') as fd:
        long_description = fd.read()
except Exception:
    long_description = ''

setup(
    name='bitchute-dl',
    version='1.0.4',
    license='MIT',
    author='Matteljay',
    author_email='matteljay@pm.me',
    description='Download any BitChute video to your PC',
    long_description = long_description,
    long_description_context_type = 'text/markdown',
    scripts = [ 'bitchute-dl' ],
    install_requires=['lxml'],
    keywords=['bitchute', 'downloader', 'youtube-dl', 'video', 'archive'],
    url='https://libersystems.com',
    download_url='https://github.com/Matteljay/bitchute-dl/releases',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

# EOF
