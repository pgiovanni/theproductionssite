import sys
from pprint import pprint
sys.path.append('/usr/local/lib/python3.8/site-packages')

import ptvsd
ptvsd.enable_attach(('localhost', 9999),redirect_output=True) 
ptvsd.wait_for_attach()


from flask import Flask, Response, render_template, request


application = Flask(__name__)
app = application


@app.route('/')
def index():
    return Response(response='hello, world! I\'m a dumb web application', status=200)


@app.route('/test_template')
def test_template():
    req = request
    return render_template('child_template.html')