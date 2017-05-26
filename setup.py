import os
import sys
from setuptools import setup, find_packages

__version__ = '0.1'

setup(name='k8sh',
      version=__version__,
      description='kubectl interactive shell',
      author='ejether',
      author_email='ejether@hotmail.com',
      install_requires=[
        "PyYAML==3.12"
      ],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: Information Technology',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Natural Language :: English',
          'Operating System :: POSIX',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: System :: Installation/Setup',
          'Topic :: System :: Systems Administration',
          'Topic :: Utilities',
      ],
      scripts=[
         'k8sh',
         ],
      )
