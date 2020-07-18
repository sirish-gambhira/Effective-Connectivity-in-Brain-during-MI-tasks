import random
import os
from get_data import get_data
from preprocess import preprocess
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
import pandas as pd
from pandas.plotting import autocorrelation_plot
from pyitlib import discrete_random_variable as drv
from idtxl.estimators_jidt import JidtGaussianTE
    
def NTE_Measure(x,y,maxlen):
    p = 0
    n = len(y)
    settings = {}
    settings['history_target'] = maxlen
    settings['tau_sources'] = 2
    net = JidtGaussianTE(settings)
    for i in range(30):
        idx = np.random.permutation(1750)
        x_shuffle = x[idx]
        p = p + net.estimate(x_shuffle,y)
    p = p/30
    texy = net.estimate(x,y)
    info = drv.entropy_conditional(y[1:n],y[0:n-1], estimator = "MINIMAX")
    return (texy-p)/info

def NTE(filepath,index):
    y = preprocess(filepath,index)
    
    history_len = 0
    
    for i in range(9):
        ax = autocorrelation_plot(y[i,:])
        ax.set_xlim([0,13])
    
    '''
        Set history_len to be max positive value for which autocorrelation is >=0
    '''
    
    A = np.zeros((9,9))
    for i in range(9):
        for j in range(9):
            A[i,j] = NTE(y[i,:],y[j,:],history_len)
            
    threshold = 0.25
    
    #Adjust threshold a/c to requirement
    
    B = A

    for i in range(9):
        for j in range(9):
            if B[i][j]<threshold:
                B[i][j] = 0
                
    return B
    
