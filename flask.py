#!/usr/bin/env python
# coding: utf-8

import json
import os
from flask import Flask, render_template
from flask import render_template_string
from flask import Flask, jsonify, request
from flask_cors import CORS

from App import Model

app = Flask(__name__)
CORS(app)

@app.route("/kmeans/", methods=['GET'])
def kmeans():
    result = Model().kmeans()
    return jsonify(result)

@app.route("/isolation/", methods=['GET'])
def isolation():
    result = Model().isolation()
    return jsonify(result)

@app.route("/hbos/", methods=['GET'])
def hbos():
    result = Model().hbos()
    return jsonify(result)

@app.route("/",methods=['GET'])
def default():
    print('Entering Default')
    return render_template('index.html')

if __name__ == "__main__":
    app.config["TEMPLATES_AUTO_RELOAD"] = True;
    app.run(debug=False)




