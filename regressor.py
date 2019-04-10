# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 10:34:44 2019

@author: NH
"""

import numpy as np 
import matplotlib.pyplot as plt
from scipy import stats

def predict_costs(month):
    print("Method called ")
    costs_rice = np.random.randint(2350,2370,1500)
    costs_cabage = np.random.randint(500,515,1500)
    costs_brinjal = np.random.randint(930,950,1500)
    months = np.random.randint(1,13,1500)
    costs = {}
    
    selling_price_rice = costs_rice + np.random.uniform(0.1,0.12,1500)
    slope,intercept,r_value,p_value,std_err = stats.linregress(months,selling_price_rice)
    costs['rice'] = slope * month + intercept
    
    selling_price_rice = costs_cabage + np.random.uniform(0.1,0.12,1500)
    slope,intercept,r_value,p_value,std_err = stats.linregress(months,selling_price_rice)
    costs['cabbage'] = slope * month + intercept
    
    selling_price_rice = costs_brinjal + np.random.uniform(0.1,0.12,1500)
    slope,intercept,r_value,p_value,std_err = stats.linregress(months,selling_price_rice)
    costs['brinjal'] = slope * month + intercept

    return costs

