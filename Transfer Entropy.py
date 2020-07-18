import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

from preprocess import preprocess
from get_data import get_data
from scipy import signal
from scipy.signal import butter, sosfilt, sosfreqz
from filters import butter_fir_filter
from statsmodels.graphics.tsaplots import plot_acf
from pandas.plotting import autocorrelation_plot
from idtxl.bivariate_te import BivariateTE
from idtxl.data import Data
from idtxl.visualise_graph import plot_network

''' Observe Effective Connectivity using IDTxl package
    Max_history length is a hyperparameter chosen by observing the autocorrelation plots of the time-series data
    Jidt Gaussian CMI is used as the estimator, as the surrogate distribution can be estimated for gaussian sources easily
    
'''
y = preprocess(filepath,index)
  
for i in range(9):
  ax = autocorrelation_plot(y[0,i,:])
  ax.set_xlim([0,13])
  
'''
Author - P. Wollstadt, J. T. Lizier, R. Vicente, C. Finn, M. Martinez-Zarzuela, P. Mediano, L. Novelli, M. Wibral 
Title - IDTxl Source Code
Availability - https://github.com/pwollstadt/IDTxl.git
'''

data = Data(y,dim_order = 'rps')

network_analysis = BivariateTE()

settings = {'cmi_estimator': 'JidtGaussianCMI',
            'max_lag_sources': max_history_length,
            'min_lag_sources': 1,
            'tau_sources': 2,
            'tau_target': 2}

results = network_analysis.analyse_network(settings=settings, data=data)

results.print_edge_list(weights='max_te_lag', fdr=False)
plot_network(results=results, weights='max_te_lag', fdr=False)
plt.show()
    