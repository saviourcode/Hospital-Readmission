#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import os from pml
from flask import Flask, render_template
from flask import render_template_string
from flask import Flask, jsonify, request
from flask_cors import CORS
import pickle
from App import Model


# In[5]:


# Loading the pickle file
model_new = pickle.load(open('model.pkl','rb'))


# In[6]:


app = Flask(__name__)
CORS(app)

@app.route("/kmeans/", methods=['GET'])
def kmeans():
    result = model_new.kmeans()
    return jsonify(result)

@app.route("/isolation/", methods=['GET'])
def isolation():
    result = model_new.isolation()
    return jsonify(result)

@app.route("/hbos/", methods=['GET'])
def hbos():
    result = model_new.hbos()
    return jsonify(result)

@app.route("/",methods=['GET'])
def default():
    print('Entering Default')
    return render_template("index.html")


# In[ ]:


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.config["TEMPLATES_AUTO_RELOAD"] = True;
    app.run(host='0.0.0.0', port=port)


# In[ ]:




