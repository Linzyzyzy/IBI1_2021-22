import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator

fig = plt.figure(figsize=(10,10),dpi=100)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.5, hspace=0.5)

covid_data = pd.read_csv("full_data.csv")
print(covid_data.iloc[10:21,0:3:2])

judge_Afghanistan = []
for i in range(len(covid_data)):
    if covid_data.iloc[i,1] == "Afghanistan":
        judge_Afghanistan.append(True)
    else:
        judge_Afghanistan.append(False)
print(covid_data.loc[judge_Afghanistan,"total_cases"])

judge_China = []
for i in range(len(covid_data)):
    if covid_data.iloc[i,1] == "China":
        judge_China.append(True)
    else:
        judge_China.append(False)
China_new_data = covid_data.iloc[judge_China,[0,2,3]]
China_dates = China_new_data.iloc[:,0]
China_new_cases = China_new_data.iloc[:,1]
China_new_deaths = China_new_data.iloc[:,2]
print(f'The mean of the China_new_cases is {np.mean(China_new_cases)}\nThe mean of the China_new_deaths is {np.mean(China_new_deaths)}')

plt.subplot(2,3,1)
plt.boxplot(China_new_cases,showfliers=False,labels=['China new cases'])
plt.ylabel('number of China new cases')
plt.title('Boxplot of China new cases')

plt.subplot(2,3,2)
plt.boxplot(China_new_deaths,showfliers=False,labels=['China new deaths'])
plt.ylabel('number of China new deaths')
plt.title('Boxplot of China new deaths')

plt.subplot(2,3,3)
plt.plot(China_dates, China_new_cases, 'b')
plt.xticks(China_dates.iloc[0:len(China_dates):4],rotation=-90,fontsize=5)
plt.ylabel('number of China new cases')
plt.title('The change with time of China new cases')

plt.subplot(2,3,4)
plt.plot(China_dates, China_new_deaths, 'r')
plt.xticks(China_dates.iloc[0:len(China_dates):4],rotation=-90,fontsize=5)
plt.ylabel('number of China new deaths')
plt.title('The change with time of China new deaths')

judge_date = []
for i in range(len(covid_data)):
    if covid_data.iloc[i,0] == "2020-03-31":
        judge_date.append(True)
    else:
        judge_date.append(False)
latest_data = covid_data.iloc[judge_date,:]
sorted_latest_data = latest_data.iloc[np.argsort(latest_data.iloc[:,4])[-6:],:]

ax1 = fig.add_subplot(2,3,5)
total_width, n = 0.6, 2  
width = total_width / n 
x = [0, 1, 2, 3, 4, 5]
ax1.bar(x, sorted_latest_data.iloc[:,4], label = 'Total cases', tick_label = sorted_latest_data.iloc[:,1], width = width, fc = 'orange')
for i in range(len(x)):
    x[i] = x[i] + width
ax1.set_ylabel("whole cases")
plt.legend(loc='upper left',fontsize=8)
plt.xticks(rotation=45,fontsize=9)
ax2 = ax1.twinx()
ax2.bar(x, sorted_latest_data.iloc[:,5], label = 'Total deaths', width = width, fc = 'blue')
for i in range(len(x)):
    x[i] = x[i] + width
ax2.set_ylabel("whole death")
plt.title('Top countries (consist of world)')
plt.legend(loc='upper right',fontsize=8)
plt.show()