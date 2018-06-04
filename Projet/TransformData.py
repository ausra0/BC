from Import import *
import numpy as np 

# --- Convert into per Serving Size 
df['Calories'] = df['Calories']/df['ServSize']
df['TotalFat'] = df['TotalFat']/df['ServSize']
df['TransFat'] = df['TransFat']/df['ServSize']
df['SatFat'] = df['SatFat']/df['ServSize']
df['Sodium'] = df['Sodium']/(df['ServSize']*1000)
df['Carbohydrates'] = df['Carbohydrates']/df['ServSize']
df['Cholesterol'] = df['Cholesterol']/(df['ServSize']*1000)
df['Fibre'] = df['Fibre']/df['ServSize']
df['Sugars'] = df['Sugars']/df['ServSize']
df['Protein'] = df['Protein']/df['ServSize']
df['VitaminA'] = df['VitaminA']*0.0009/(100*df['ServSize']) # DV : 900 mcg
df['VitaminC'] = df['VitaminC']*0.06/(100*df['ServSize']) # DV : 60 mg
df['Calcium'] = df['Calcium']/(100*df['ServSize']) # DV : 1 g 
df['Iron'] = df['Iron']*0.018/(100*df['ServSize']) # DV : 18 mg

# --- Add features 
df['HFat'] = df['TotalFat'] - (df['SatFat'] + df['TransFat'])

# --- Scale and center
df['Calories'] = (df['Calories']-(np.mean(df['Calories'])))/np.sqrt(np.var(df['Calories']))
df['TransFat'] = (df['TransFat']-(np.mean(df['TransFat'])))/np.sqrt(np.var(df['TransFat']))
df['TotalFat'] = (df['TotalFat']-(np.mean(df['TotalFat'])))/np.sqrt(np.var(df['TotalFat']))
df['SatFat'] = (df['SatFat']-(np.mean(df['SatFat'])))/np.sqrt(np.var(df['SatFat']))
df['Sodium'] = (df['Sodium']-(np.mean(df['Sodium'])))/np.sqrt(np.var(df['Sodium']))
df['Carbohydrates'] = (df['Carbohydrates']-(np.mean(df['Carbohydrates'])))/np.sqrt(np.var(df['Carbohydrates']))
df['Cholesterol'] = (df['Cholesterol']-(np.mean(df['Cholesterol'])))/np.sqrt(np.var(df['Cholesterol']))
df['Fibre'] = (df['Fibre']-(np.mean(df['Fibre'])))/np.sqrt(np.var(df['Fibre']))
df['Sugars'] = (df['Sugars']-(np.mean(df['Sugars'])))/np.sqrt(np.var(df['Sugars']))
df['Protein'] = (df['Protein']-(np.mean(df['Protein'])))/np.sqrt(np.var(df['Protein']))
df['VitaminA'] = (df['VitaminA']-(np.mean(df['VitaminA'])))/np.sqrt(np.var(df['VitaminA']))
df['VitaminC'] = (df['VitaminC']-(np.mean(df['VitaminC'])))/np.sqrt(np.var(df['VitaminC']))
df['Calcium'] = (df['Calcium']-(np.mean(df['Calcium'])))/np.sqrt(np.var(df['Calcium']))
df['Iron'] = (df['Iron']-(np.mean(df['Iron'])))/np.sqrt(np.var(df['Iron']))
df['HFat'] = (df['HFat']-(np.mean(df['HFat'])))/np.sqrt(np.var(df['HFat']))


#df['SugarProCal'] = df['Sugars']/(1 + df['Calories'])

#del df['Sodium']
#del df['SatFat']
#print(df.columns.values)

