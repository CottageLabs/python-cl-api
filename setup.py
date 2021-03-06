from setuptools import setup, find_packages
import sys

setup(
    name = 'python-cl-api',
    version = '1.0.0',
    packages = find_packages(),
    install_requires = [
        "octopus==1.0.0",
        "esprit",
        "Flask",
        # for deployment
        "gunicorn",
        "newrelic",
    ] + (["setproctitle"] if "linux" in sys.platform else []),
    url = 'http://cottagelabs.com/',
    author = 'Cottage Labs',
    author_email = 'us@cottagelabs.com',
    description = 'Python tools and utilities to support the CL API',
    classifiers = [
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
