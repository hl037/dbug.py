#!/usr/bin/env python
import sys

from setuptools import setup, find_packages


def read_file(name):
    """
    Read file content
    """
    f = open(name)
    try:
        return f.read()
    except IOError:
        print("could not read %r" % name)
        f.close()

LONG_DESC = read_file('README.rst') + '\n\n' + read_file('HISTORY.rst')

EXTRAS = {}

if sys.version_info > (3,):
    EXTRAS['use_2to3'] = True

setup(
    name='dbug',
    version='1.0b5',
    description='Print tools for debuging',
    long_description=LONG_DESC,
    author='Léo Flaventin Hauchecorne',
    author_email='hl037.prog@gmail.com',
    url='http://leo-flaventin.com',
    project_urls={
      'Documentation': 'https://github.com/hl037/dbug.py/blob/master/dbug/__init__.py',
      'Source': 'https://github.com/hl037/dbug.py',
      'Tracker': 'https://github.com/hl037/dbug.py/issues',
    },
    license='Public Domain',
    packages=find_packages(),
    test_suite=None,
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    extras_require=None,
    entry_points=None,
    classifiers=[
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'License :: Public Domain',
      'Programming Language :: Python',
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 3',
      'Topic :: Software Development :: Debuggers',
    ],
    **EXTRAS
)
