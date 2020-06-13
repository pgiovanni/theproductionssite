import sys
from pprint import pprint
sys.path.append('/usr/local/lib/python3.8/site-packages')

from flask import Flask, Response, render_template, request

application = Flask(__name__)
app = application


@app.route('/')
def index():
    return Response(response=render_template('index.html'), status=200)

@app.route('/child_templates/<html_name>')
def html_reciever(html_name):
    return Response(response=render_template(html_name), status=200)

@app.template_global()
def path_to_styles(filename):
    return '/music-site/styles/' + filename

@app.template_global()
def path_to_scripts(filename):
    return '/music-site/scripts/' + filename

@app.template_global()
def path_to_images(filename):
    return '/music-site/images/' + filename

@app.template_global()
def path_to_templates(filename):
    return '/webapp/child_templates/' + filename

@app.template_global()
def path_to_music(filename):
    return '/music-site/music/' + filename



