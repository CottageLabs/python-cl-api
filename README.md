# Python CL API

Python tools and utilities to support the CL API

## Installation

Clone the project:

    git clone https://github.com/CottageLabs/python-cl-api.git

get all the submodules

    cd python-cl-api
    git submodule update --init --recursive
    
This will initialise and clone the esprit and magnificent octopus libraries, and their submodules in turn.

Create your virtualenv and activate it

    virtualenv /path/to/venv
    source /path/tovenv/bin/activate

Install the dependencies and this app in the correct order:

    cd python-cl-api
    pip install -r requirements.txt
    
Create your local config

    cd python-cl-api
    touch local.cfg

Then you can override any config values that you need to

To start the application, you'll also need to install it into the virtualenv just this first time

    cd python-cl-api
    pip install -e .

Then, start your app with

    python service/web.py

If you want to specify your own root config file, you can use

    APP_CONFIG=path/to/rootcfg.py python service/web.py
    
