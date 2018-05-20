###################################################
#################### SESSION 8 ####################
###################################################
# --- IMPORTS
from S8tools import model1
from S8tools import model2 
from S8tools import generateX 
import matplotlib.pyplot as plt 

# --- MAIN ()
# initialization (changable parameters) 
n = 50 
Ex = 2
Vx = 1

# generate dataset 
x = GenerateX(Ex, Vx, n)

# sample from model1 and model2 
fM1 = model1(1, 2)
y1 = fM1(x)

fM2 = model2(1, 1, 2, Ex, Vx)
y2 = fM2(x)

# plot 
fig, ax = plt.subplots()
ax.plot(x, y1, marker='.', linestyle='', ms=3, label="model 1")
ax.plot(x, y2, marker='.', linestyle='', ms=3, label="model 2")
plt.show()

