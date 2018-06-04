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
tr = dtrain[["Calories", "TransFat"]]
ytr = dtrain["Brand"]
ts = dtest[["Calories", "TransFat"]]
dft = df[["Calories", "TransFat"]]

# --- ADD INTERCEPT 
#tr.assign(ones=pd.Series([1]*len(tr), index=tr.index))
#ts.assign(ones=pd.Series([1]*len(ts), index=ts.index))
#dft.assign(ones=pd.Series([1]*len(dft), index=dft.index))

tr[1:10]
