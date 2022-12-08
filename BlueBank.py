# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 14:45:02 2022

@author: campbn2
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#method 1 to read json data
json_file = open('loan_data_json.json')
data = json.load(json_file)

#method 2 to read json data
with open('loan_data_json.json') as json_file:
        data = json.load(json_file)
        #python uses indents to seperate parts of a statement on sep lines to be more readable
        
#transform from list of dicts to dataframe
loandata = pd.DataFrame(data)

#working with unique fxn
#finding unique values in purpose column
loandata['purpose'].unique()

#describe fxn
loandata.describe()
#count is number of values
#mean is average
#std is standard deviation
#min is minimum value
#25% is 25% inter quarter range which means 25% of your data have less than this number
#50% is 50% inter quarter range which means 50% of your data have less than this number
#75% is 75% inter quarter range which means 75% of your data have less than this number
#max is maximum value

#describe for a specific column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#log.annual.inc is the log of the annual income and we'd actually like the annual income which is an exponent.  
#the numpy library has an exponent function
#first must install and then import numpy
#in admin anaconda cmd prompt, run pip install numpy to install
#import numpy as np -- do this up at the top of your script though

#using EXP to get annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income

#working with arrays
#arrays - similar to lists - data structure that stores collection of data.  ordered data, enclosed in [] and data can be non-unique.  
#unlike lists, arrays need to be declared w/ a fxn in numpy
#1D array
arr = np.array([1, 2, 3, 4])

#0D array
arr = np.array(43)

#2D array
arr=np.array([[1,2,3],[4,5,6]])


#If statements
a = 40
b = 500

if b > a:
    print('b is greater than a')
    
#lets add more conditions
a = 40
b = 500
c = 1000

if b>a and b<c:
    print('b is in betw a and c')
    
#what if a condition is not met
a = 40
b = 500
c = 20

if b>a and b<c:
    print('b is greater than a but less than c')
else:
    print('No conditions met')


#another condition, different metrics
a = 40
b = 500
c = 30

if b>a and b<c:
    print('b is greater than a but less than c')
elif b>a and b>c:
    print('b is greater than both a and c')
else:
    print('no conditions met')
    

#fico score
#for loops in python are iterative

length = len(loandata)
ficocat = [] #this is an empty list
for x in range(0,length):
    category = loandata['fico'][x]
    
    try:
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >= 401 and category < 600:
            cat = 'Poor'
        elif category >= 601 and category < 660:
            cat = 'Fair'
        elif category >= 661 and category < 700:
            cat = 'Good'
        elif category >= 700:
            cat = 'Excellent'
        else:
            cat = 'Unknown'
    except:
        cat = 'Unknown'
        
    ficocat.append(cat) #add current value of cat to the end of the ficocat list
    
ficocat = pd.Series(ficocat)  #use the pandas library to turn the ficocat list into a series (column) of the same name
loandata['fico.category'] = ficocat

#while loops

i = 0
while i <= 10:
    print(i)
    i = i+1
    
    
#df.loc as conditional statements
# df.loc[df['columnname'] condition, newcolumnname] = 'value if the condition is met'

#for interest rates, a new column is wanted.  rate > 0.12 then high, else low
loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'

#playing with plots
#number of loans/rows by fico.category
catplot = loandata.groupby(['fico.category']).size()  #from loandata, group by fico.category and count the number of rows (size())will represent that
catplot.plot.bar() #using bar because fico.category is discreet...there's only certain options...can be plotted like dates in a series
plt.show()

purposeplot = loandata.groupby(['purpose']).size()
purposeplot.plot.bar(color = 'green', width = 0.1)
plt.show()

#scatter plots
ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color = '#4caf50')
plt.show()

#writing to csv
loandata.to_csv('loan_cleaned.csv', index = True) #kepp the index in the csv because we don't have a unique identifier/key other than this





















