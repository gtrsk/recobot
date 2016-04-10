from flask import Flask, render_template, jsonify
import json
from flask.ext.triangle import Triangle
import imdb
import urllib2
import logging

app = Flask(__name__, static_path='/static')
imdb_access = imdb.IMDb()
logger = logging.getLogger('recobot')

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movie/<movieid>')
def get_movie_data(movieid):
   movie = imdb_access.get_movie(movieid)
   logger.debug('Movie' + movie.summary())
   json_obj = movie.summary()
   return json_obj

def test_logging():
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler('recobot.log')
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.debug('debug is on')
    logger.info('info is on')
    logger.warning('warning is on')

if __name__ == '__main__':
    test_logging()
    app.debug = True 
    Triangle(app)
    app.run(host='0.0.0.0', port=6999)
