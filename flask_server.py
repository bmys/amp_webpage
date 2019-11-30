import os
import json
from flask import Flask, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
@cross_origin()
def home():
     return render_template('index.html')

@app.route("/members")
@cross_origin()
def members():
     path = os.path.join('/home/pythonic/domains/pythonic.pl/public_python/static', 'players.json')
     with app.open_resource('static/data/players.json') as f:
          data = json.load(f)
          return data 
     return path 

if __name__ == "__main__":
     app.run()