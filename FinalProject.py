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

USAfont = {'family': 'serif',
        'color':  '#15488D',
        'weight': 'normal',
        'size': 16,
        }
CHINAfont = {'family': 'serif',
        'color':  '#DF3B10',
        'weight': 'normal',
        'size': 16,
        }
MEXfont = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }
BRAfont = {'family': 'serif',
        'color':  'white',
        'weight': 'normal',
        'size': 16,
        }
ITAfont = {'family': 'serif',
        'color':  'white',
        'weight': 'normal',
        'size': 16,
        }
JORfont = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }

#%% Section 1 Milestone 2 Information 
# Might remove this part
df = pd.read_csv('Covid_Data_final.csv', header=[0],parse_dates=True)

mex_cases = df.loc[df["iso_code"] == 'MEX',"total_cases"]
usa_cases = df.loc[df["iso_code"] == 'USA',"total_cases"]
chn_cases = df.loc[df["iso_code"] == 'CHN',"total_cases"]
bra_cases = df.loc[df["iso_code"] == 'BRA',"total_cases"]
ita_cases = df.loc[df["iso_code"] == 'ITA',"total_cases"]
jor_cases = df.loc[df["iso_code"] == 'JOR',"total_cases"]

mex_date = df.loc[df["iso_code"] == 'MEX', "date"]
usa_date = df.loc[df["iso_code"] == 'USA', "date"]
chn_date = df.loc[df["iso_code"] == 'CHN', "date"]
bra_date = df.loc[df["iso_code"] == 'BRA', "date"]
ita_date = df.loc[df["iso_code"] == 'ITA', "date"]
jor_date = df.loc[df["iso_code"] == 'JOR', "date"]

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
COMPARING THE VACCINATION COUNT TO THE VIRUS' MORTALITY RATE OF THESE
#USA_new_vaccinations = USA_new_vaccinations.dropna() #how='all'
#USA_new_deaths = USA_new_deaths.dropna()

#print("%f is vac length",len(USA_new_vaccinations))
#print("%f is vac length",len(USA_new_deaths))
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


""" READ INFO FOR EACH COUNTRY"""
df = pd.read_csv("Covid_Data_final.csv", names=column_names,low_memory=False,parse_dates=True)

USA_new_deaths = df.loc[df["iso_code"] == 'USA',"new_deaths_per_million"]
USA_new_vaccinations = df.loc[df["iso_code"] == 'USA',"new_vaccinations_smoothed"]

CHN_new_deaths = df.loc[df["iso_code"] == 'CHN',"new_deaths_per_million"]
CHN_new_vaccinations = df.loc[df["iso_code"] == 'CHN',"new_vaccinations_smoothed"]

MEX_new_deaths = df.loc[df["iso_code"] == 'MEX',"new_deaths_per_million"]
MEX_new_vaccinations = df.loc[df["iso_code"] == 'MEX',"new_vaccinations_smoothed"]

BRA_new_deaths = df.loc[df["iso_code"] == 'BRA',"new_deaths_per_million"]
BRA_new_vaccinations = df.loc[df["iso_code"] == 'BRA',"new_vaccinations_smoothed"]

ITA_new_deaths = df.loc[df["iso_code"] == 'ITA',"new_deaths_per_million"]
ITA_new_vaccinations = df.loc[df["iso_code"] == 'ITA',"new_vaccinations_smoothed"]

JOR_new_deaths = df.loc[df["iso_code"] == 'JOR',"new_deaths_per_million"]
JOR_new_vaccinations = df.loc[df["iso_code"] == 'JOR',"new_vaccinations_smoothed"]


"""
USA 
"""
fig = plt.figure()
fig.patch.set_facecolor('#F5755B')
plt.xlabel("Date",fontdict=USAfont)
plt.ylabel("Amount",fontdict=USAfont)
plt.bar(usa_date,USA_new_deaths,label = 'new deaths',alpha=0.5,color="#1F5E97") 
plt.bar(usa_date,USA_new_vaccinations,label = 'new vaccinations',alpha=0.5,color="#F66C28") 
plt.bar(usa_date,usa_cases,label = 'new cases',alpha=0.5,color="#FAD4A2") 

plt.legend(loc='upper right')
plt.semilogy()
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=30)) 
plt.gca().xaxis.set_tick_params(rotation = 30)
plt.title('USA Data Per Day', fontdict=USAfont)
plt.show()
"""
CHINA 
"""
fig = plt.figure()
fig.patch.set_facecolor('#E9E251')
plt.xlabel("Date",fontdict=CHINAfont)
plt.ylabel("Amount",fontdict=CHINAfont)
plt.bar(chn_date,CHN_new_deaths,label = 'new deaths',alpha=0.5,color="#1F5E97") 
plt.bar(chn_date,CHN_new_vaccinations,label = 'new vaccinations',alpha=0.5,color="#F66C28") 
plt.bar(chn_date,chn_cases,label = 'new cases',alpha=0.5,color="#FAD4A2") 

plt.legend(loc='upper right')
plt.semilogy()
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=30)) 
plt.gca().xaxis.set_tick_params(rotation = 30)
plt.title("China Daya Per Day",fontdict=CHINAfont)
plt.show()
"""
MEXICO 
"""
fig = plt.figure()
fig.patch.set_facecolor('#24770C')
plt.xlabel("Date",fontdict=MEXfont)
plt.ylabel("Amount",fontdict=MEXfont)
plt.bar(mex_date,USA_new_deaths,label = 'new deaths',alpha=0.5,color="#1F5E97") 
plt.bar(mex_date,USA_new_vaccinations,label = 'new vaccinations',alpha=0.5,color="#F66C28") 
plt.bar(mex_date,usa_cases,label = 'new cases',alpha=0.5,color="#FAD4A2") 

plt.legend(loc='upper right')
plt.semilogy()
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=30)) 
plt.gca().xaxis.set_tick_params(rotation = 30)
plt.title('Mexico Data Per Day', fontdict=MEXfont)
plt.show()
"""
BRAZIL 
"""
fig = plt.figure()
fig.patch.set_facecolor('#0C6CA1')
plt.xlabel("Date",fontdict=BRAfont)
plt.ylabel("Amount",fontdict=BRAfont)
plt.bar(bra_date,BRA_new_deaths,label = 'new deaths',alpha=0.5,color="#1F5E97") 
plt.bar(bra_date,BRA_new_vaccinations,label = 'new vaccinations',alpha=0.5,color="#F66C28") 
plt.bar(bra_date,bra_cases,label = 'new cases',alpha=0.5,color="#FAD4A2") 

plt.legend(loc='upper right')
plt.semilogy()
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=30)) 
plt.gca().xaxis.set_tick_params(rotation = 30)
plt.title('Brazil Data Per Day', fontdict=BRAfont)
plt.show()
"""
ITALY
"""
fig = plt.figure()
fig.patch.set_facecolor('#E74C3C')
plt.xlabel("Date",fontdict=ITAfont)
plt.ylabel("Amount",fontdict=ITAfont)
plt.bar(ita_date,ITA_new_deaths,label = 'new deaths',alpha=0.5,color="#1F5E97") 
plt.bar(ita_date,ITA_new_vaccinations,label = 'new vaccinations',alpha=0.5,color="#F66C28") 
plt.bar(ita_date,ita_cases,label = 'new cases',alpha=0.5,color="#FAD4A2") 

plt.legend(loc='upper right')
plt.semilogy()
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=30)) 
plt.gca().xaxis.set_tick_params(rotation = 30)
plt.title('Italy Data Per Day', fontdict=ITAfont)
plt.show()
"""
JORDAN
"""
fig = plt.figure()
fig.patch.set_facecolor('#F22D1E')
plt.xlabel("Date",fontdict=JORfont)
plt.ylabel("Amount",fontdict=JORfont)
plt.bar(jor_date,JOR_new_deaths,label = 'new deaths',alpha=0.5,color="#1F5E97") 
plt.bar(jor_date,JOR_new_vaccinations,label = 'new vaccinations',alpha=0.5,color="#F66C28") 
plt.bar(jor_date,jor_cases,label = 'new cases',alpha=0.5,color="#FAD4A2") 

plt.legend(loc='upper right')
plt.semilogy()
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=30)) 
plt.gca().xaxis.set_tick_params(rotation = 30)
plt.title('Jordan Data Per Day', fontdict=JORfont)
plt.show()

#%% Section 4 Natalie
# Impact the vaccine has on the hospitalization rate of countries
