# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 18:27:34 2022

@author: campbn2
"""

import pandas as pd

# file_name = pd.read_csv('file.csv') <---- format of read_csv

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv',sep=';')

#summary of the data

data.info()

#playing with variables
var = 'hello world'

#working with calculations

#defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

#math operations on tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem
SellingPricePerTransaction = SellingPricePerItem * NumberOfItemsPurchased
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

#costpertransaction column calc
#CostPerTransaction = CostPerItem * NumberOfItemsPurchased
# variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

#adding new column to dataframe

data['CostPerTransaction'] = CostPerTransaction

data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

#Sales per transaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#profit calc = sales - cost

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#markup - (sales-cost)/cost

data['Markup'] = (data['ProfitPerTransaction'] ) / data['CostPerTransaction']

#Rounding markup

roundmarkup = round(data['Markup'], 2)

data['Markup'] = round(data['Markup'], 2)

#combining data fields

my_name = 'nikki' + 'campbell'

# data['Date'] = data['Day'] + '-' + data['Month'] + '-' + data['Year'] doesn't work b/c year and day are integers and you cannot concat strings w/ integers.  types must be same.


#checking columns data type
print(data['Day'].dtype)

#Change columns type

day = data['Day'].astype(str)
print(day.dtype)

data['Date'] = data['Day'].astype(str) + '-' + data['Month'] + '-' + data['Year'].astype(str)


#using iloc to view specific columns/rows

data.iloc[0] #views row w/ index = 0 which is auto added into table when you bring data into python

data.iloc[0:3] #brings in first 3 rows
data.iloc[-5:] #brings in last five rows
data.head(5) #brings in first 5 rows
data.iloc[:,2]  # :, represents all rows for column 2; everything starts with 0, so column 2 is the third column
data.iloc[4,2] #fourth row in second column

#using split to split client key words field
#new_var = column.str.split('sep' , expand = True) ...expand means it will go through every comma in the field, not just the first.
split_col = data['ClientKeywords'].str.split(',' , expand = True)

#creating new columns for split_col
data['Client Age'] = split_col[0] # column 0
data['ClientAge'] = split_col[0] # column 0
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

#made a mistake and called column Client Space Age and now i have two client age columns.  need to delete the one with the space in the name
data.pop('Client Age')

#use replace fxn to get ride  of extranious characters in client age
data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']' , '')

#changing itemdescription to lower case using the lower function
data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files
#bringing in a new data set

seasons = pd.read_csv('value_inc_seasons.csv',sep=';')

#merging files:  merge_df = pd.merge(df_old, DF_new, on = 'key') key is common field between the two dataframes

data = pd.merge(data, seasons, on = 'Month')

#dropping day, month, year colunms as well as ClientKeyWords
# df = df.drop('columnname' , axis = 1) 1 means column and 0 means row
data = data.drop('ClientKeywords' , axis = 1)
data = data.drop('Day' , axis = 1)
data = data.drop('Month' , axis = 1)
data = data.drop('Year' , axis = 1)

#dropping mult columns at once
# data = data.drop(['Year','Month'], axis = 1)



#export to csv
data.to_csv('ValueInc_Cleaned.csv', index = False) #don't include the index column (we don't need this because we have transaction ID which is a unique number)































































