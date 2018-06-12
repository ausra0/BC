# CREATES TRAIN AND TEST SETS FROM DATASET 

# --- IMPORTS 
from TransformData import *
import numpy as np
import numpy.random as rdm 

# --- MAIN()
# cut the dataset
dtrain = df.sample(frac=0.8, random_state=32)
dtest = df.drop(dtrain.index)

# --- TRIM TRAIN AND TEST SET :
"""
tr = dtrain[["Calories", "TransFat"]]
ytr = dtrain["Brand"]
ts = dtest[["Calories", "TransFat"]]
dft = df[["Calories", "TransFat"]]
"""
tr = dtrain[["Calories", "Carbohydrates"]]
ytr = dtrain["Brand"]
ts = dtest[["Calories", "Carbohydrates"]]
dft = df[["Calories", "Carbohydrates"]]
"""
tr = dtrain[["Calories", "TotalFat"]]
ytr = dtrain["Brand"]
ts = dtest[["Calories", "TotalFat"]]
dft = df[["Calories", "TotalFat"]]
"""

# --- ADD INTERCEPT 
#tr = tr.assign(ones=pd.Series([1]*len(tr), index=tr.index))
#ts = ts.assign(ones=pd.Series([1]*len(ts), index=ts.index))
#dft = dft.assign(ones=pd.Series([1]*len(dft), index=dft.index))

