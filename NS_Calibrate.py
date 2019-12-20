#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: winstonsmith22
"""
import numpy as np
import pandas as pd
from nelson_siegel_svensson.calibrate import calibrate_ns_ols

# fixed array
t = np.arange(1,10.5,0.5)

# import timeseries with pandas
timeseries = pd.read_excel('/Users/alexbennett/Desktop/pptimeseries.xlsx')
length = len(timeseries)
parameters = np.empty([length,4])

# reset
b0 = 0
b1 = 0
b2 = 0
tau = 0
idx = 0
error = 0

for idx in range(0, length):
    y = timeseries[idx:idx+1]
    y = y.to_numpy()
    y = y.reshape((19,))

    try:
        curve, status = calibrate_ns_ols(t, y, tau0=1.0)  # starting value of 1.0 for the optimisation of tau
        if status.success == 1:
            b0 = curve.beta0
            b1 = curve.beta1
            b2 = curve.beta2
            tau = curve.tau
            iteration = np.array([b0,b1,b2,tau])
            iteration = iteration.reshape(1,4)
            parameters[idx] = iteration
        else:
            iteration = np.array([0,0,0,0])
            parameters[idx] = iteration
            error = error+1
    except:
         iteration = np.array([0,0,0,0])
         parameters[idx] = iteration
         error= error+1


#parametersexport = pd.DataFrame(parameters)
#parametersexport.to_excel('parameters2.xlsx', index=False)
         
print("the sweet taste of success...")
