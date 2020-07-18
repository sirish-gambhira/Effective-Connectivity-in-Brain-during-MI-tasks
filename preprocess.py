import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

from get_data import get_data
from scipy import signal
from scipy.signal import butter, sosfilt, sosfreqz
from filters import butter_fir_filter


def preprocess(filepath,index):    
    
    PATH = filepath
    index = index
    '''
        Subject indices are from [1,9]
    '''
    
    data1,label = get_data(index,True,PATH)
    
    left = 1.0
    '''
        Left Hand Motor imagery tasks are denoted by 1.0. Similarly right hand MI tasks are denoted by 2.0
    '''
    
    '''
        Collecting all indices with required condition and averaged to eliminate noise and bias
    '''
    cond = np.where(label==left)[0]
    
    
    S = np.zeros((1,9,1750))
    
    for i in range(cond.shape[0]):
        S[0,0,:] = S[0,0,:] + data1[cond[i],0,:]
        S[0,1,:] = S[0,1,:] + data1[cond[i],1,:]
        S[0,2,:] = S[0,2,:] + data1[cond[i],5,:]
        S[0,3,:] = S[0,3,:] + data1[cond[i],7,:]
        S[0,4,:] = S[0,4,:] + data1[cond[i],9,:]
        S[0,5,:] = S[0,5,:] + data1[cond[i],11,:]
        S[0,6,:] = S[0,6,:] + data1[cond[i],13,:]
        S[0,7,:] = S[0,7,:] + data1[cond[i],17,:]
        S[0,8,:] = S[0,8,:] + data1[cond[i],19,:]
    S = S/len(cond)
    
    
    '''
    Bandpassing the signal with 8-30Hz filter
    '''
    
    #fs = Sampling frequency
    fs = 250
    f_bands = np.zeros((1,2)).astype(float)
    f_bands[0] = [5,30]
    
    #Normalising the frequency band
    f = f_bands[:1]/fs
    
    #Creating band-pass filter
    filter_bank = np.zeros((1,4,6))
    filter_bank[0] = butter(4, f[0], analog=False, btype='band', output='sos')
    
    y = np.zeros((1,9,1750))
    
    for i in range(9):
        y[0,i,:] = sosfilt(filter_bank[0],S[0,i,:])
    
    return y
  
