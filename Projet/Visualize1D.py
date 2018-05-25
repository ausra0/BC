from TestTrain import *
# dtrain is the name of the dataset containg the dataset

import matplotlib.pyplot as plt
import sys

# get variables form terminal call 
total = len(sys.argv)
# get the input variables
params = sys.argv
# export to parameters 
param1 = params[1]

def visual(param1):
    # group the data in the different categories 
    groups = dtrain.groupby('Brand')

    # define companies dictionnary 
    dic = {-1 : 'McDo', 1: 'Starbucks'}
    
    # define bins 
    a = min(dtrain.loc[:, param1])
    b = max(dtrain.loc[:, param1])
    bins = np.linspace(a, b, 50)

    # do the plot
    fig, ax = plt.subplots()
    for name, group in groups:
        # ax.plot(getattr(group, param1), marker='.', linestyle='', ms=3, label=dic[name])
        ax.hist(getattr(group, param1), bins, alpha=0.5, label=dic[name])
        ax.legend()
    plt.suptitle('Histogram of '+param1+' (per g. of food)')
    plt.xlabel(param1)
    #plt.ylabel()
    plt.show()

# test if correct number of input variables, if yes, call function
if(not(total-2)):
    visual(param1)
