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


print("Rows in file:",len(df))  
print("Columns in file:",len(df.axes[1])) 
print("USA days represented:",len(usa_cases)) 
print("China days represented:",len(chn_cases)) 
print("Brazil days represented:",len(bra_cases)) 
print("Italy days represented:",len(ita_cases)) 
print("Jordan days represented:",len(jor_cases)) 

# End of Milestone2 Information/data
#%% Section 2 Eric
# Compare country's vaccnation data to number of day-to-day cases 
#from March 2021 to October 2021 to analyze how the vaccine impacts covid cases
#Mexico graph
mex_cases = df.loc[df["iso_code"] == 'MEX',"total_cases"]
mex_new = df.loc[df["iso_code"] == 'MEX',"new_cases"]
mex_vacc = df.loc[df["iso_code"] == 'MEX',"new_vaccinations_smoothed"]

date = df.loc[df["iso_code"] == 'MEX', "date"]

plt.bar(date,mex_vacc, label = 'Vaccination', color='darkred')
plt.bar(date,mex_new, label = 'New Cases', color='lightcoral')

plt.legend()
plt.semilogy()
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=30)) 
plt.gca().xaxis.set_tick_params(rotation = 30)
plt.title('Mexico Daily Chart')
plt.show()

#Italy graph
ita_cases = df.loc[df["iso_code"] == 'ITA',"total_cases"]
ita_new = df.loc[df["iso_code"] == 'ITA',"new_cases"]
ita_vacc = df.loc[df["iso_code"] == 'ITA',"new_vaccinations_smoothed"]

date = df.loc[df["iso_code"] == 'MEX', "date"]

plt.bar(date,ita_vacc, label = 'Vaccination', color='darkorchid')
plt.bar(date,ita_new, label = 'New Cases', color='orchid')

plt.legend()
plt.semilogy()
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=30)) 
plt.gca().xaxis.set_tick_params(rotation = 30)
plt.title('Italy Daily Chart')
plt.show()

#Brazil graph
bra_cases = df.loc[df["iso_code"] == 'BRA',"total_cases"]
bra_new = df.loc[df["iso_code"] == 'BRA',"new_cases"]
bra_vacc = df.loc[df["iso_code"] == 'BRA',"new_vaccinations_smoothed"]

date = df.loc[df["iso_code"] == 'MEX', "date"]

plt.bar(date,bra_vacc, label = 'Vaccination', color='gray')
plt.bar(date,bra_new, label = 'New Cases', color='lightgray')

plt.legend()
plt.semilogy()
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=30)) 
plt.gca().xaxis.set_tick_params(rotation = 30)
plt.title('Brazil Daily Chart')
plt.show()

#China graph
chn_cases = df.loc[df["iso_code"] == 'CHN',"total_cases"]
chn_new = df.loc[df["iso_code"] == 'CHN',"new_cases"]
chn_vacc = df.loc[df["iso_code"] == 'CHN',"new_vaccinations_smoothed"]

date = df.loc[df["iso_code"] == 'MEX', "date"]


plt.bar(date,chn_vacc, label = 'Vaccination', color='darkgoldenrod')
plt.bar(date,chn_new, label = 'New Cases', color='gold')

plt.legend()
plt.semilogy()
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=30)) 
plt.gca().xaxis.set_tick_params(rotation = 30)
plt.title('China Daily Chart')
plt.show()

#Jordan graph
jor_cases = df.loc[df["iso_code"] == 'JOR',"total_cases"]
jor_new = df.loc[df["iso_code"] == 'JOR',"new_cases"]
jor_vacc = df.loc[df["iso_code"] == 'JOR',"new_vaccinations_smoothed"]

date = df.loc[df["iso_code"] == 'MEX', "date"]

plt.bar(date,jor_vacc, label = 'Vaccination', color='darkgreen')
plt.bar(date,jor_new, label = 'New Cases', color='palegreen')

plt.legend()
plt.semilogy()
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=30)) 
plt.gca().xaxis.set_tick_params(rotation = 30)
plt.title('Jordan Daily Chart')
plt.show()

#USA graph
usa_cases = df.loc[df["iso_code"] == 'USA',"total_cases"]
usa_new = df.loc[df["iso_code"] == 'USA',"new_cases"]
usa_vacc = df.loc[df["iso_code"] == 'USA',"new_vaccinations_smoothed"]

date = df.loc[df["iso_code"] == 'MEX', "date"]

plt.bar(date,usa_vacc, label = 'Vaccination', color='navy')
plt.bar(date,usa_new, label = 'New Cases', color='royalblue')

plt.legend()
plt.semilogy()
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=30)) 
plt.gca().xaxis.set_tick_params(rotation = 30)
plt.title('USA Daily Chart')
plt.show()

#%% Section 3 Steph
"""
COMPARING THE VACCINATION COUNT TO THE VIRUS' MORTALITY RATE OF
- USA
- CHINA
- MEXICO
- ITALY
- BRAZIL
- JORDAN
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
plt.title("China Data Per Day",fontdict=CHINAfont)
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

#read file
df = pd.read_csv("Covid_Data_final.csv", index_col=0)

#Vaccination and Hospital Admission rate for USA, Israel, Denmark, Portugal, Italy, and Latvia
weekly_date = df.dropna(subset=['weekly_hosp_admissions_per_million']) #Got weekly dates first


USA_new_vaccinations = weekly_date.loc['USA', "new_vaccinations_smoothed"]
USA_hospital_admissions = weekly_date.loc['USA', "weekly_hosp_admissions_per_million"]
USA_weekly_date = weekly_date.loc['USA', "date"]

ISR_new_vaccinations = weekly_date.loc['ISR', "new_vaccinations_smoothed"]
ISR_hospital_admissions = weekly_date.loc['ISR', "weekly_hosp_admissions_per_million"]
ISR_weekly_date = weekly_date.loc['ISR', "date"]

DNK_new_vaccinations = weekly_date.loc['DNK', "new_vaccinations_smoothed"]
DNK_hospital_admissions = weekly_date.loc['DNK', "weekly_hosp_admissions_per_million"]
DNK_weekly_date = weekly_date.loc['DNK', "date"]

PRT_new_vaccinations = weekly_date.loc['PRT', "new_vaccinations_smoothed"]
PRT_hospital_admissions = weekly_date.loc['PRT', "weekly_hosp_admissions_per_million"]
PRT_weekly_date = weekly_date.loc['PRT', "date"]

ITA_new_vaccinations = weekly_date.loc['ITA', "new_vaccinations_smoothed"]
ITA_hospital_admissions = weekly_date.loc['ITA', "weekly_hosp_admissions_per_million"]
ITA_weekly_date = weekly_date.loc['ITA', "date"]

LVA_new_vaccinations = weekly_date.loc['LVA', "new_vaccinations_smoothed"]
LVA_hospital_admissions = weekly_date.loc['LVA', "weekly_hosp_admissions_per_million"]
LVA_weekly_date = weekly_date.loc['LVA', "date"]


#USA graph 
fig = plt.figure()

x_axis = np.arange(len(USA_weekly_date))

plt.bar(x_axis, USA_new_vaccinations, 0.4, color=['red'], label ='Vaccinations')
plt.bar(x_axis, USA_hospital_admissions, 0.4, color=['blue'], label= 'Hospital Admissions')


plt.xticks(x_axis, USA_weekly_date)
plt.tick_params(axis='x', labelrotation=50)
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5)) 
plt.title("Fig 2: USA- Vaccinations vs. Hospitalizations")
plt.xlabel("Dates")
plt.ylabel("Amount")
plt.legend(loc='center right')
plt.annotate("Figure 2", (10,10))

plt.semilogy()
plt.show()

#Israel graph 
fig = plt.figure()

x_axis = np.arange(len(ISR_weekly_date))

plt.bar(x_axis, ISR_new_vaccinations, 0.4, color=['red'], label ='Vaccinations')
plt.bar(x_axis, ISR_hospital_admissions, 0.4, color=['blue'], label= 'Hospital Admissions')

plt.xticks(x_axis, ISR_weekly_date)
plt.tick_params(axis='x', labelrotation=50)
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5)) 
plt.title("Fig 3: Israel- Vaccinations vs. Hospitalizations")
plt.xlabel("Dates")
plt.ylabel("Amount")
plt.legend(loc='center right')
plt.semilogy()
plt.show()

#Denmark graph 
fig = plt.figure()

x_axis = np.arange(len(DNK_weekly_date))

plt.bar(x_axis, DNK_new_vaccinations, 0.4, color=['red'], label ='Vaccinations')
plt.bar(x_axis, DNK_hospital_admissions, 0.4, color=['blue'], label= 'Hospital Admissions')

plt.xticks(x_axis, DNK_weekly_date)
plt.tick_params(axis='x', labelrotation=50)
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5)) 
plt.title("Fig 4: Denmark- Vaccinations vs. Hospitalizations")
plt.xlabel("Dates")
plt.ylabel("Amount")
plt.legend(loc='center right')
plt.semilogy()
plt.show()

#Portugal graph 
fig = plt.figure()

x_axis = np.arange(len(PRT_weekly_date))

plt.bar(x_axis, PRT_new_vaccinations, 0.4, color=['red'], label ='Vaccinations')
plt.bar(x_axis, PRT_hospital_admissions, 0.4, color=['blue'], label= 'Hospital Admissions')

plt.xticks(x_axis, PRT_weekly_date)
plt.tick_params(axis='x', labelrotation=50)
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5)) 
plt.title("Fig 5: Portugal- Vaccinations vs. Hospitalizations")
plt.xlabel("Dates")
plt.ylabel("Amount")
plt.legend(loc='center right')
plt.semilogy()
plt.show()

#Italy graph 
fig = plt.figure()

x_axis = np.arange(len(ITA_weekly_date))

plt.bar(x_axis, ITA_new_vaccinations, 0.4, color=['red'], label ='Vaccinations')
plt.bar(x_axis, ITA_hospital_admissions, 0.4, color=['blue'], label= 'Hospital Admissions')

plt.xticks(x_axis, ITA_weekly_date)
plt.tick_params(axis='x', labelrotation=50)
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5)) 
plt.title("Fig 6: Italy- Vaccinations vs. Hospitalizations")
plt.xlabel("Dates")
plt.ylabel("Amount")
plt.legend(loc='center right')
plt.semilogy()
plt.show()

#Latvia graph 
fig = plt.figure()

x_axis = np.arange(len(LVA_weekly_date))

plt.bar(x_axis, LVA_new_vaccinations, 0.4, color=['red'], label ='Vaccinations')
plt.bar(x_axis, LVA_hospital_admissions, 0.4, color=['blue'], label= 'Hospital Admissions')

plt.xticks(x_axis, LVA_weekly_date)
plt.tick_params(axis='x', labelrotation=50)
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5)) 
plt.title("Fig 7: Latvia- Vaccinations vs. Hospitalizations")
plt.xlabel("Dates")
plt.ylabel("Amount")
plt.legend(loc='center right')
plt.semilogy()
plt.show()
