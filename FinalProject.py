# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 15:10:06 2021

@author: boaxi
"""
# Include imports, files, and such here
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv('Covid Data final.csv', header=[0],parse_dates=True)


# Milestone 2 Information 
# Might remove this part
mex_cases = df.loc[df["iso_code"] == 'MEX',"total_cases"]
usa_cases = df.loc[df["iso_code"] == 'USA',"total_cases"]
chn_cases = df.loc[df["iso_code"] == 'CHN',"total_cases"]
bra_cases = df.loc[df["iso_code"] == 'BRA',"total_cases"]
ita_cases = df.loc[df["iso_code"] == 'ITA',"total_cases"]

mex_date = df.loc[df["iso_code"] == 'MEX', "date"]
usa_date = df.loc[df["iso_code"] == 'USA', "date"]
chn_date = df.loc[df["iso_code"] == 'CHN', "date"]
bra_date = df.loc[df["iso_code"] == 'BRA', "date"]
ita_date = df.loc[df["iso_code"] == 'ITA', "date"]

countries = ['Mexico','USA','China','Brazil','Italy']

fig = plt.figure()
plt.xlabel("Date")
plt.ylabel("Total Cases")

plt.plot(mex_date,mex_cases)      
plt.plot(usa_date,usa_cases) 
plt.plot(chn_date,chn_cases)
plt.plot(bra_date,bra_cases)
plt.plot(ita_date,ita_cases)

#plt.semilogy()
plt.legend(countries)
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=30)) 
plt.gca().xaxis.set_tick_params(rotation = 30)

plt.show()
     
# End of Milestone2 Information/data

# Eric
# Compare country's vaccnation data to number of day-to-day cases 
#from March 2021 to October 2021 to analyze how the vaccine impacts covid cases







# Steph
# Comparing the vaccination count to the virus' mortality rate of these countries







# Natalie
# Impact the vaccine has on the hospitalization rate of countries


