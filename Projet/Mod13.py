# --- IMPORTS : 
#basis
import pickle 
import matplotlib.pyplot as plt
import pandas as pd
#own (X)
from TestTrain import *
from Mod11 import *

# --- LOAD DATA : (X)
with open("./output/M1.dat", "rb") as file:
	[exp, IC] = pickle.load(file)


# --- TRAIN ERROR : 
err = 0
ninv = 1/(2*len(tr)) # /2 because values in +/-1
pred = []
for i in tr.index.values:
    true_val = dtrain.loc[i,'Brand']
    pred_val = indcond(exp, i, flag)
    pred.append(pred_val) # save this value
    err += abs(true_val - pred_val)*ninv

print("Error on training set : "+str(err))


# Append predicted and true values to data
assert len(tr)==len(pred)
assert len(tr)==len(ytr)
tr = tr.assign(pred=pd.Series(pred, index=tr.index))
tr = tr.assign(tval=ytr)



# --- DISPLAY MISSCLASSIFICATIONS : 
param1 = list(tr)[0]
param2 = list(tr)[1]

def visual_error(param1, param2):
    # group the data in the different categories
    groups = tr.groupby(("tval", "pred"))

    # define companies dictionnary
    dic = {(-1, -1) : "McDo ok", (1, 1): "Starbucks ok", (-1, 1) : "Was McDo", (1, -1) : "Was SB"}

    # do the plot
    _, ax = plt.subplots()
    for name, group in groups:
        ax.plot(getattr(group, param1), getattr(group, param2), marker='.', linestyle='', ms=3, label=dic[name])
        ax.legend()
    plt.suptitle(param1+' vs '+param2+' (per g. of food)')
    plt.xlabel(param1)
    plt.ylabel(param2)
    plt.savefig("./plots/error_mod1.png")
    plt.show()

# PLOT
visual_error(param1, param2)
visual(param1, param2, exp)
