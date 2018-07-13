import pandas as pd
import numpy as np
df=pd.read_csv("weather.csv")
print(df)
#first 5 row of dataframe
print(df.head(5))
#first 10 rows of dataframe
print(df.head(10))

#find basic functionalities of ststics on particular dataframe
#print mean of dataframe
print(df.mean())
#print meadian
print(df.median())
#print mode
print(df.mode())

# #print standard deviation
print(df.std())
#print variance
print(df.var())

#print last five row of dataframes
print(df.tail(5))

#print 3rd column and perform statics onit
print(df.columns)
df=(df.iloc[:,1:2])
print(df.describe())