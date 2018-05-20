# --- IMPORTS : 
#basis
import pickle 
import matplotlib.pyplot as plt
import pandas as pd
#own (X)
from TestTrain import *
from Mod11 import *

# --- LOAD DATA : (X)
with open("./output/M2.dat", "rb") as file:
	[exp, IC] = pickle.load(file)


# --- TRAIN ERROR : 
err = 0
ninv = 1/(2*len(tr))
pred = []
for i in range(0, len(tr)):
    true_val = dtrain["Brand"].iloc[i]
    pred_val = 2*rdm.binomial(1, indcond(exp, i))-1
    pred.append(pred_val) # save this value
    err += abs(true_val - pred_val)*ninv

print("Error on training set : "+str(err))


# Append predicted and true values to data
tr['pred']=pd.Series(pred)
tr['true']=pd.Series(dtrain['Brand'])


# --- DISPLAY MISSCLASSIFICATIONS : 
param1 = 'Calories' #(X)
param2 = 'TransFat' #(X)

def visual(param1, param2):
    # group the data in the different categories
    groups = tr.groupby(('true', 'pred'))

    # define companies dictionnary
    dic = {(-1, -1) : 'McDo ok', (1, 1): 'Starbucks ok', (-1, 1) : 'Was McDo', (1, -1) : 'Was SB'}

    # do the plot
    fig, ax = plt.subplots()
    for name, group in groups:
        ax.plot(getattr(group, param1), getattr(group, param2), marker='.', linestyle='', ms=3, label=dic[name])
        ax.legend()
    plt.suptitle(param1+' vs '+param2+' (per g. of food)')
    plt.xlabel(param1)
    plt.ylabel(param2)
    plt.show()

# PLOT
visual(param1, param2)
