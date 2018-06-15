# CREATES TRAIN AND TEST SETS FROM DATASET 

# --- IMPORTS 
from TransformData import *
import numpy as np
import numpy.random as rdm 

#rdm.seed(32)

# --- MAIN()
# cut the dataset
dtrain = df.sample(frac=0.7, random_state=32)
dtest = df.drop(dtrain.index)

# --- TRIM TRAIN AND TEST SET :
"""
tr = dtrain[["Calories", "TransFat"]]
ytr = dtrain["Brand"]
ts = dtest[["Calories", "TransFat"]]
yts = dtest['Brand']
dft = df[["Calories", "TransFat"]]
"""
tr = dtrain[["Calories", "Carbohydrates"]]
ytr = dtrain["Brand"]
ts = dtest[["Calories", "Carbohydrates"]]
yts = dtest['Brand']
dft = df[["Calories", "Carbohydrates"]]
"""
tr = dtrain[["Calories", "TotalFat"]]
ytr = dtrain["Brand"]
ts = dtest[["Calories", "TotalFat"]]
yts = dtest['Brand']
dft = df[["Calories", "TotalFat"]]
"""

# --- CREATE OUTLIERS DATASETS 
"""
fract = 0.1 # fraction of outliers 

victims = ytr.sample(frac = fract, random_state = 32).index
ytrout = ytr
ytrout.loc[victims] = -1*ytrout.loc[victims]
"""

# --- ADD INTERCEPT 
#tr = tr.assign(ones=pd.Series([1]*len(tr), index=tr.index))
#ts = ts.assign(ones=pd.Series([1]*len(ts), index=ts.index))
#dft = dft.assign(ones=pd.Series([1]*len(dft), index=dft.index))

