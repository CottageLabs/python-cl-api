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

Then you can override any config values that you need to (though you shouldn't need to with this app).


## Running

This app is designed to provide supporting tools to the CL API. Some are exposed via the web, some are command line tools.

Command line scripts can be executed using the runner:

    python magnificent-octopus/octopus/bin/run.py [command] [arguments]

Capabilities exposed over the network (like the CSV file parser) can be accessed after running the web daemon. This can be set up as usual on review and live servers with nginx and supervisord, or accessed directly on dev envs:

    python service/web.py

### CSV reading:

See: magnificent-octopus/octopus/modules/sheets/README.md
