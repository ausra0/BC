# --- IMPORTS
import pandas as pd
import csv
import sys

# --- MANAGE SCRIPT INPUT
# get variables form terminal call 
total = len(sys.argv)
if(total==2):
    # get the input variables
    params = sys.argv
    # define conversion function 
    def str2bool(v):
        return v.lower() in ("yes", "true", "t", "1")
    # export to parameters 
    flag1 = str2bool(params[1])
else: 
    flag1 = False


# --- SCRIPT CORE
# import data from CSV 
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    li = list(reader)

# extract the titles of coluns
header = li[0]
li = li[1:]

header = ['Brand', 'Item', 'ServSize', 'Calories', 'TotalFat', 'TransFat', 'SatFat', 'Sodium', 'Carbohydrates', 'Cholesterol', 'Fibre', 'Sugars', 'Protein', 'VitaminA', 'VitaminC', 'Calcium', 'Iron']

# convert data into pands dataframe
df = pd.DataFrame(li, columns=header, dtype='float')

# remap Brand classification 
# MacDo = -1
# Starbucks = 1
df['Brand'] = df['Brand'].map({1: 1, 0:-1})

if(flag1):
    # display attributes (for reference while running other programs)
    print('Attributes for this dataset :')
    print(header)
    print(df[1:10])
