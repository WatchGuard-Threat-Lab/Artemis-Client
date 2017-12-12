import sys
import os

os.environ["MPLCONFIGDIR"] = "." 

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

install_requires = [
    'hpfeeds',
    'gevent',
    'python-daemon',
]

config = {
    'name':'artemis-client',
    'description': 'Thug for Artemis honeynet',
    'url':'https://github.com/WatchGuard-Threat-Lab/artemis-client',
    'author':'Marc Laliberte',
    'version':'1.0.0',
    'install_requires': install_requires,
    'license':'GPLv3',
}

setup(**config)
