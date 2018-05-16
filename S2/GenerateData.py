import numpy as np
import matplotlib.pyplot as plt 
import random as rdm 

def GenerateDataset(n):
    """ 
    GENERATEDATASET generates a dataset along some distribution
    :param n: (scalar) nb of pts. 
    :param f: (function handle) function along which to sample 
    :return: 
    """ 
    data = np.zeros((n, 2))
    for i in range(0, n): 
        data[i, 0] = round(rdm.random())
        data[i, 1] = 10*rdm.random()
    return data 

