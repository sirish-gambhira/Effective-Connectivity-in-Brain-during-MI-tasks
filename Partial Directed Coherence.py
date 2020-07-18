import os
import numpy as np
import connectivipy as cp
from preprocess import preprocess
from MEMD_all import memd

'''
Key Arguements:
    Function to get adjacency matrix corresponding to top 10 Effective connectivity estimated by Partial Directed Coherence
'''
def PDC(filepath,index):

    y = preprocess(filepath,index)
    
    imf = memd(y)
    #returns a 3D matrix 'imf(M,N,L)' containing M multivariate IMFs, one IMF per column, computed by applying
    #the multivariate EMD algorithm on the N-variate signal (time-series) X of length L.
    
    '''
        IMF1 is shown to contain maximum information content among the estimated IMFs, hence taken.
    '''
    
    IMF1 = imf[0,:,:]
    
    model_coeff, reflection_matrix = cp.mvarmodel.Mvar.fit(IMF1, order = None, method = 'ns')
    PDC = cp.conn.pdc_fun(model_coeff,reflection_matrix,250,512)
    PDC = np.square(PDC)
    
    
    '''
        Out-in rates are calculated and corresponding ratios are estimated for all channels.
    '''
    
    delta = np.zeros((512,9)).astype(float)
    out_info = np.zeros((512,9)).astype(float)
    in_info = np.zeros((512,9)).astype(float)
    
    for f in range(512):
        for i in range(9):
            s = 0
            for j in range(9):
                s += PDC[f,j,i]
            out_info[f,i] = s
            r = 0
            for k in range(9):
                r = r + PDC[f,i,k]
            in_info[f,i] = r
            delta[f,i] = out_info[f][i]/in_info[f][i]
        
    '''
        Spectral points in the frequency range from [13-25](Beta Band) are taken to study effective connectivity.
    '''
    p = np.zeros((9,9))
    A = np.zeros((9,9))
    f = np.linspace(0,125,num = 512)
    count = 0
    for (ind,f) in enumerate(f):
        if f>=13 and f<=25:
            p = p + PDC[ind,:,:]
            count = count + 1
        if f>25:
            break
    p = p/count
    
    
    '''
        Top 10 ECs in the PDC are estimated and corresponding adjacency matrix is returned.
    '''
       
    ii = np.unravel_index(np.argsort(p.ravel())[-30:], p.shape)
    count = 0
    for i in range(30):
        if ii[1][29-i]!= ii[0][29-i]:
            A[ii[1][29-i]][ii[0][29-i]] = 1
            print(ii[0][29-i],ii[1][29-i])
            count = count + 1
        if count == 10:
            break
    
    return A
