#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 10:14:27 2019

@author: alexbennett
"""

import numpy as np
import pandas as pd
from nelson_siegel_svensson import NelsonSiegelCurve
from statistics import mean


t = np.arange(1,10.5,0.5)

timeseries = pd.read_excel('/Users/alexbennett/Desktop/pptimeseries.xlsx')
parameters = pd.read_excel('/Users/alexbennett/Desktop/parameters.xlsx')

parameters2 = parameters.to_numpy()

length = len(timeseries)
correlations = np.empty([length,1])
estimatearray = np.empty([length,19])
counter = 0

for counter in range(0,length):
    beta0 = parameters2[counter,0]
    beta1 = parameters2[counter,1]
    beta2 = parameters2[counter,2]
    tau0 = parameters2[counter,3]

    k = NelsonSiegelCurve(beta0,beta1,beta2,tau0)

    estimate = k(t) 
    true_row = timeseries[counter:counter+1]
    true_row = true_row.to_numpy()
    true = true_row.reshape((19,))

    estimatearray[counter] = true_row

    corr = np.corrcoef(estimate,true)
    correlations[counter] = corr[0,1]
    
correlations = correlations[~np.isnan(correlations)]
average = mean(correlations)
minimum = min(correlations)
maximum = max(correlations)
    

# plot 
#idx = 2156
#estimatetoplot = estimatetoplot.reshape((19,))
#estimatetoplot = estimatearray[idx:idx+1]
#truetoplot = timeseries[idx:idx+1]
#truetoplot = truetoplot.to_numpy()
#truetoplot = truetoplot.reshape((19,))

print("success") 