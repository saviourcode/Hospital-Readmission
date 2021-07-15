#!/usr/bin/env python
# coding: utf-8

# ### Importing Libraries

# In[1]:


import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.ensemble import IsolationForest
from pyod.models.hbos import HBOS
from sklearn import cluster
import sqlite3


# ### Reading Data from Database

# In[2]:


con = sqlite3.connect('healthcare.db')


# In[3]:


df = pd.read_sql_query("Select * from healthcare", con)


# In[4]:


con.close()


# In[5]:


df.head()


# ### Model Building

# In[10]:


class Model:

    # KMeans Clustering
    def kmeans(data = df):
        kmeans = KMeans(n_clusters=2)

        df['Readmission'] = kmeans.fit_predict(df[['Age', 'Gender', 'Smoker', 'Prevalent_Stroke', 'Prevalent_Hyp', 'Diabetes',
                                           'Cholestrol', 'SysBP', 'DiaBP', 'BMI', 'Heart_Rate', 'Glucose', 'Diet_Followed',
                                           'Med_Followed', 'Calories_Burnt', 'Steps']])

        kmeans.cluster_centers_

        # Patient requiring readmission
        return ('No. of patients to be readmitted using KMeans:', df[df['Readmission'] == 1].shape[0])
    
    # Isolation Forest
    def isolation(data = df):   
        clf = IsolationForest(random_state=0)

        df['Readmission'] = clf.fit_predict(df[['Age', 'Gender', 'Smoker', 'Prevalent_Stroke', 'Prevalent_Hyp', 'Diabetes',
                                           'Cholestrol', 'SysBP', 'DiaBP', 'BMI', 'Heart_Rate', 'Glucose', 'Diet_Followed',
                                           'Med_Followed', 'Calories_Burnt', 'Steps']])

        # overall_dataset[(df['Diet_Followed'] == 0) & (df['Readmission'] == 1)]
        return ('No. of patients to be readmitted using Isolation Forest:', df[df['Readmission'] == 1].shape[0])

    # HBOS
    def hbos(data = df):
        clf = HBOS()

        df['Readmission'] = clf.fit_predict(df[['Age', 'Gender', 'Smoker', 'Prevalent_Stroke', 'Prevalent_Hyp', 'Diabetes',
                                           'Cholestrol', 'SysBP', 'DiaBP', 'BMI', 'Heart_Rate', 'Glucose', 'Diet_Followed',
                                           'Med_Followed', 'Calories_Burnt', 'Steps']])

        return ('No. of patients to be readmitted using HBOS:', df[df['Readmission'] == 1].shape[0])


# In[11]:


model = Model()


# In[14]:


model.hbos()


# In[ ]:




