# --- IMPORTS : 
from TransformData import * 
import numpy as np 
import matplotlib.pyplot as plt 

# --- COMPUTE MATRIX OF CORRELATIONS : 
dfc = df.iloc[:, 3:]
cm = dfc.corr().as_matrix()


# --- PLOT THE MATIRX :
# set figure size (for nice export)
plt.figure(figsize=(20,20))

# plot the background colors
plt.title("Correlation matrix")
plt.imshow(np.abs(cm), interpolation="None", cmap=plt.cm.Blues)
plt.colorbar()

# plot the category names
target_names = [lab for lab in dfc.columns]
name_anchors = np.arange(len(target_names)) 
plt.xticks(name_anchors, target_names, rotation=90)
plt.yticks(name_anchors, target_names)

# plot the confusion percentages, as text
# we need to change the text color based on the background color
# if the background is above a threshold, we use white as text color
thresh = cm.max() / 2.
for i in range(len(target_names)):
    for j in range(len(target_names)): 
        plt.text(i, j, "{:.2f}".format(cm[i, j]), horizontalalignment="center", color="white" if cm[i, j] > thresh else "black")

plt.tight_layout()

plt.savefig("./plots/correlation_matrix.png", dpi=300, bbox_inches="tight")
plt.show()
