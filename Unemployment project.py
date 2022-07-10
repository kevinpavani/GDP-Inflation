import pandas as pd
import matplotlib.pyplot as plt
import csv
import matplotlib.dates
from datetime import datetime
from sklearn.linear_model import LinearRegression
import numpy as np

# Setting with copy warning disables
pd.options.mode.chained_assignment = None

#PART 1 - GDP

#Load Data
gdp = pd.read_csv(r'C:\Users\kevin\OneDrive\Desktop\Python projects\Unemployment Italy\GDP.csv')

#Get rid of columns we don't need
del gdp["Series Name"]
del gdp["Series Code"]
del gdp["Country Name"]
del gdp["Country Code"]


#Transpose horizontal data
gdp = pd.read_csv(r'C:\Users\kevin\OneDrive\Desktop\Python projects\Unemployment Italy\GDP.csv', skiprows=0, header=None).T   # Read csv, and transpose
gdp.columns = gdp.iloc[0]
gdp.drop(5,inplace=True)


#Visualize actual value, no scientific notation (e+)
#We use Python formatter with zero decimal places and the thousand comma separator
pd.options.display.float_format ='{:,0f}'.format

#Noticed a very messy data, need to remove the first 5 rows
gdp2 = gdp.iloc[5: , ]

#Get rid of extra columns we don't need
gdp2.dropna(how='all', axis=1, inplace=True)


#Rename Columns
gdp2.rename(columns = {'Series Name':'Year', 'GDP (current US$)':'GDP'}, inplace=True)

#Messy Data, ex: 2012 is set as 2012 [YR2012]
gdp2.at[6,'Year'] = 2012
gdp2.at[7,'Year'] = 2013
gdp2.at[8,'Year'] = 2014
gdp2.at[9,'Year'] = 2015
gdp2.at[10,'Year'] = 2016
gdp2.at[11,'Year'] = 2017
gdp2.at[12,'Year'] = 2018
gdp2.at[13,'Year'] = 2019
gdp2.at[14,'Year'] = 2020
gdp2.at[15,'Year'] = 2021


#Transformed Years into dates
gdp2['Year'] = pd.to_datetime(gdp2['Year'], format= '%Y')

#Transformed values into float
gdp2['GDP'] = list(map(float, gdp2['GDP']))


plt.plot(gdp2['Year'],gdp2['GDP'], marker = 'o', linestyle = 'solid', color = '#5F9EA0')
plt.title('GDP Italy 2012-2021', color = '#FF7F50')
plt.xlabel('Year',  color = '#FF7F50')
plt.ylabel('GDP (in $tn)',  color = '#FF7F50')

#Incline Dates to make it visually attractive
plt.gcf().autofmt_xdate()

plt.show()


#PART 2 - UNEMPLOYMENT

inflation = pd.read_csv(r'C:\Users\kevin\OneDrive\Desktop\Python projects\Unemployment Italy\Inflation 5.csv')


#Transpose Data
inflation = pd.read_csv(r'C:\Users\kevin\OneDrive\Desktop\Python projects\Unemployment Italy\Inflation 5.csv', skiprows=0, header=None).T
inflation.columns = inflation.iloc[0]

#Messy data, remove first row
inflation = inflation.iloc[1:,]


#Get rid of extra columns we don't need
#inflation.dropna(how='all', axis=1, inplace=True)

#Rename Columns
inflation.rename(columns = {'Country Name':'Year', 'Italy':'Inflation'}, inplace=True)

#Transformed Years into dates
inflation['Year'] = pd.to_datetime(inflation['Year'], format= '%Y')

#Transformed values into float, also removed some weird dot thousands separator
#inflation['Inflation'] = inflation['Inflation'].str.replace(',', '')
#inflation['Inflation'] = inflation['Inflation'].str.replace('.', '')
#inflation = inflation.astype({'Change':'float'})
#inflation['Change'] = inflation['Change'].str.rstrip('%').astype('float')

#Transform inflation values into float and then integer, also replaced comma with dot
inflation['Change'] = inflation['Change'].str.replace(',', '.')
inflation = inflation.astype({'Change':'float'})
inflation = inflation.astype({'Change':'int'})



#print(inflation.to_string())
#print(inflation.info())
#print(inflation.dtypes)

#Plot Inflation and Year
plt.plot(inflation['Year'],inflation['Change'], marker = 'o', linestyle = 'solid', color = 'darkcyan')
plt.title('Inflation Italy 2012-2021', color = 'slategray')
plt.xlabel('Year',  color = 'slategray')
plt.ylabel('Inflation (in %)',  color = 'slategray')
plt.ylim([-1,4])
plt.gcf().autofmt_xdate()
plt.show()

#Subplot
plt.subplot(1,2,1)
plt.plot(gdp2['Year'],gdp2['GDP'])
plt.title('GDP', color = '#FF7F50')
plt.gcf().autofmt_xdate()

plt.subplot(1,2,2)
plt.plot(inflation['Year'],inflation['Change'])
plt.title('Inflation', color = 'slategray')
plt.ylim([-1,4])
plt.gcf().autofmt_xdate()

plt.suptitle('Italy 2012-2021')

plt.show()

# Calculate Correlation
corr = inflation['Change'].corr(gdp2['GDP'])
print(corr)

