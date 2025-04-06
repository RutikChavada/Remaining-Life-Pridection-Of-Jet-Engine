import streamlit as st
import mysql.connector
import pandas as pd
import numpy as np
import random
import time
import plotly.express as px
import joblib

# Define the list of features
feature_columns = [
    'set1',
    'set2',
    'sensor2',
    'sensor3',
    'sensor4',
    'sensor6',
    'sensor7',
    'sensor8',
    'sensor9',
    'sensor11',
    'sensor12',
    'sensor13',
    'sensor14',
    'sensor15',
    'sensor17',
    'sensor20',
    'sensor21'
]

# Define the min, max, mean values for each feature based on your statistics.
feature_stats = {
    'set1':    {'min': -0.0087, 'max': 0.0087,   'mean': -0.000009},
    'set2':    {'min': -0.0006, 'max': 0.0006,   'mean': 0.000002},
    'sensor2': {'min': 641.21,  'max': 644.53,   'mean': 642.680934},
    'sensor3': {'min': 1571.04, 'max': 1616.91,  'mean': 1590.523119},
    'sensor4': {'min': 1382.25, 'max': 1441.49,  'mean': 1408.933782},
    'sensor6': {'min': 21.60,   'max': 21.61,    'mean': 21.609803},
    'sensor7': {'min': 549.85,  'max': 556.06,   'mean': 553.367711},
    'sensor8': {'min': 2387.90, 'max': 2388.56,  'mean': 2388.096652},
    'sensor9': {'min': 9021.73, 'max': 9244.59,  'mean': 9065.242941},
    'sensor11':{'min': 46.85,   'max': 48.53,    'mean': 47.541168},
    'sensor12':{'min': 518.69,  'max': 523.38,   'mean': 521.413470},
    'sensor13':{'min': 2387.88, 'max': 2388.56,  'mean': 2388.096152},
    'sensor14':{'min': 8099.94, 'max': 8293.72,  'mean': 8143.752722},
    'sensor15':{'min': 8.3249,  'max': 8.5848,   'mean': 8.442146},
    'sensor17':{'min': 388.0,   'max': 400.0,    'mean': 393.210654},
    'sensor20':{'min': 38.14,   'max': 39.43,    'mean': 38.816271},
    'sensor21':{'min': 22.8942, 'max': 23.6184,  'mean': 23.289705}
}



def generate_sensor_data():
    """
    Generate sensor readings for each feature using the defined min and max.
    (You can modify this function to use other distributions if desired.)
    """
    print("column add")
    return {col: random.uniform(feature_stats[col]['min'], feature_stats[col]['max'])
            for col in feature_columns}