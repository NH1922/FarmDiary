# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 11:21:46 2019

@author: NH
"""

import numpy as np 
import pandas as pd 
from scipy import stats

def predict_expenses():
    daily_expenses = np.random.uniform(100,1500,1500)
    days = np.random.uniform(1,29,1500)
    rough_expense = daily_expenses + np.random.uniform(1,29,1500)
    slope,intercept,r_value,p_value,std_err = stats.linregress(rough_expense,days)
    total_expenses = 0
    for i in range(29):
        prediction = slope * i + intercept
        total_expenses = total_expenses + prediction
    return total_expenses * 30