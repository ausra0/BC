# Project description : 
Project for Bayesian Computation course. 

# Important Remark : 
File sections that need attention when copying, renaming files are maked with (X). That can be found easily in vim : /(X)

# Data : 
Fats are divided into 3 categories : total fats (unsaturate + saturated + trans), saturates (animal products, unhealthy), transfat (good fats that have been saturated wwith hydrogen to extend shelf life, induces bad cholesterol)

# Content of the folder : 
## Undocumented : 
Prior.py  
CondDist.py   

## Import and treat data : 
|FILE			|DESCRIPTION				|
|:----------------------|:--------------------------------------|
|data.csv		|our data				|
|Import.py		|importing the data (pandas)		|
|TransformData.py	|add/remove features			|
|TestTrain.py		|separate testing and training datasets	|

## Data visualisation : 
|FILE			|DESCRIPTION 				|
|:----------------------|:--------------------------------------|
|Visualize.py		|make plots of the data  		|
|AutoRun.py 		|run Visalize.py for all features 	|

## Methods : 
|FILE 			|DESCRIPTION				|
|:----------------------|:--------------------------------------|
|Methods1.py		|sampling (IS and AR)			|
|Methods2.py		|sampling (MH) 				|
|Methods3.py 		|optimization (GD, LSGD, Newton, SGD)	|
|Methods4.py		|Laplace approximation			|

## Main file (script): 
|FILE			|DESCRIPTION				|
|:----------------------|:--------------------------------------|
|Model.py		|script for presentation at the exam  	|



# Documentation of scripts :

## AutoRun.py
Enables to visualize the whole data set projected on 2 feature space.  
Used to remove not useful features.  
-- requires :  
	TranformData.py  
	Visualize.py  

## Import.py 
Imports the dataset from .csv file using pandas  
Data is transormed (features deleted/added) in TransformData.py  

## Methods1.py
Importance Sampling and Acceptance Rejection scripts  

## Methods2.py 
Metropolis-Hastings methods (with and without burn-in period)  

## Model.py 
## SamplingMethods.py
## TestTrain.py
## TranssformData.py

## Visualize.py 
Enables 2D visualization of the dataset  
-- if 2 arguments :  
	Does the scatter of param1 vs param2  
	AND displays the name of the features of the dataset  
-- else :  
	Displays the name of the features of the dataset  

