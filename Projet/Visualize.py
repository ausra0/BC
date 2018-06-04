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
param2 = params[2]

def visual(param1, param2):
    # group the data in the different categories 
    groups = dtrain.groupby('Brand')

    # define companies dictionnary 
    dic = {-1 : 'McDo', 1: 'Starbucks'}

    # do the plot
    fig, ax = plt.subplots()
    for name, group in groups:
        ax.plot(getattr(group, param1), getattr(group, param2), marker='.', linestyle='', ms=3, label=dic[name])
        ax.legend()
    plt.suptitle(param1+' vs '+param2+' (per g. of food)')
    plt.xlabel(param1)
    plt.ylabel(param2)
    plt.show()

# test if correct number of input variables, if yes, call function
if(not(total-3)):
    visual(param1, param2)
