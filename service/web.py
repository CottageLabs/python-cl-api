from octopus.core import app, initialise, add_configuration
from octopus.modules.sheets import commasep
from flask import request
from StringIO import StringIO
import uuid

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true", help="pycharm debug support enable")
    parser.add_argument("-c", "--config", help="additional configuration to load (e.g. for testing)")
    args = parser.parse_args()

    if args.config:
        add_configuration(app, args.config)

    pycharm_debug = app.config.get('DEBUG_PYCHARM', False)
    if args.debug:
        pycharm_debug = True

    if pycharm_debug:
        app.config['DEBUG'] = False
        import pydevd
        pydevd.settrace(app.config.get('DEBUG_SERVER_HOST', 'localhost'), port=app.config.get('DEBUG_SERVER_PORT', 51234), stdoutToServer=True, stderrToServer=True)
        print "STARTED IN REMOTE DEBUG MODE"

    initialise()

# most of the imports should be done here, after initialise()
#from flask import render_template
#from octopus.lib.webapp import custom_static

"""
# this allows us to override the standard static file handling with our own dynamic version
@app.route("/static/<path:filename>")
def static(filename):
    return custom_static(filename)
"""

@app.route('/csv2obj', methods=['POST'])
def csv2obj():
    csvfile = request.files[request.files.keys()[0]]
    # TODO use octopus.modules.sheets.sheets.ObjectByRow . But it needs
    # enhancing with being able to define a spec by itself, rather than
    # having one passed into it.

@app.route('/csv2utf8str', methods = ['POST'])
def csv2utf8str():
    f = request.files[request.files.keys()[0]]
    tmpfn = str(uuid.uuid4())
    tmppath = '/tmp/{0}'.format(tmpfn)
    f.save(tmppath)

    reader = commasep.CsvReader(tmppath)
    result = StringIO()
    writer = commasep.CsvWriter(result)
    writer.write(reader.read(), close=False)
    return result.getvalue()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=app.config['PORT'], threaded=False)

