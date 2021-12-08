# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 15:10:06 2021

@author: Eric, Steph, Natalie
"""
# Include imports, files, and such here
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

#%% Section 1 Milestone 2 Information 
# Might remove this part
df = pd.read_csv('Covid_Data_final.csv', header=[0],parse_dates=True)

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
#%% Section 2 Eric
# Compare country's vaccnation data to number of day-to-day cases 
#from March 2021 to October 2021 to analyze how the vaccine impacts covid cases
#%% Section 3 Steph
"""
COMPARING THE VACCINATION COUNT TO THE VIRUS' MORTALITY RATE OF THESE COUNTRIES

Parameters
----------
data : dict or dict-like
    Data used to populate the new Series.
index : Index or index-like, default None
    Index for the new Series: if None, use dict keys.
dtype : dtype, default None
    The dtype for the new Series: if None, infer from data.

Returns
-------
_data : BlockManager for the new Series
index : index for the new Series
"""

#Read column names into array
column_names = ["iso_code","continent","location","date","total_cases",
                "new_cases","total_deaths","new_deaths","total_cases_per_million",
                "new_cases_per_million","total_deaths_per_million",
                "new_deaths_per_million","icu_patients","icu_patients_per_million",
                "hosp_patients","hosp_patients_per_million","weekly_icu_admissions",
                "weekly_icu_admissions_per_million","weekly_hosp_admissions",
                "weekly_hosp_admissions_per_million","new_vaccinations_smoothed","population"
                ,"median_age","aged_65_older","aged_70_older","cardiovasc_death_rate"]


#read file
df = pd.read_csv("Covid_Data_final.csv", names=column_names,low_memory=False,parse_dates=True)


#USA new deaths & new vaccinations
USA_new_deaths = df.loc[df["iso_code"] == 'USA',"new_deaths_per_million"]
USA_new_vaccinations = df.loc[df["iso_code"] == 'USA',"new_vaccinations_smoothed"]


USA_new_vaccinations = USA_new_vaccinations.dropna() #how='all'
USA_new_deaths = USA_new_deaths.dropna()

print("%f is vac length",len(USA_new_vaccinations))
print("%f is vac length",len(USA_new_deaths))



plt.bar(USA_new_deaths,USA_new_vaccinations)  
plt.show()



#%% Section 4 Natalie
# Impact the vaccine has on the hospitalization rate of countries
