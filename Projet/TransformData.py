from Import import *

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

#df['SugarProCal'] = df['Sugars']/(1 + df['Calories'])

#del df['Sodium']
#del df['SatFat']
#print(df.columns.values)

