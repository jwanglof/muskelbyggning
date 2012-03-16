from flask import Flask
app = Flask("muskelbyggning")
app = Flask(__name__.split('.')[0])
# http://flask.pocoo.org/docs/api/#flask.Flask

import muskelbyggning.views
