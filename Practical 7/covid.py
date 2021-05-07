#use os work with files and directories and pandas to work with dataframes
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#The code for importing the .csv file

os.chdir("/Users/a1234/study")
# os.chdir()=cd

covid_data = pd.read_csv("full_data.csv")
#every second row between 0 and 10
a=covid_data.iloc[0:12:2,:]
print(a)

#use Boolean to show “total cases” for all rows corresponding to Afghanistan
covid_data.loc[(covid_data["location"] == 'Afghanistan'), ["total_cases"]]
data1=[]
for i in range (0,7996):
	if covid_data.iloc[i,1]=="Afghanistan":
            # to choose data in covid_data with "location" showing "Afghanistan" 
		data1.append(True)
	else:
		data1.append(False)
b=covid_data.loc[data1,"total_cases"]
print(b)

#worldwide new cases
data2= []
for i in range (0,7996):
     if covid_data.iloc[i,1]=="World":
         #choose data in covid_data with "location" showing "World"
             data2.append(True)
     else:
             data2.append(False)
world_new_cases=covid_data.loc[data2,"new_cases"]

#calculate the mean and median of new cases for the entire world
mean = str(np.mean(world_new_cases))
median = str(np.median(world_new_cases))
print("the mean and median of new cases for the entire world are "+mean+" and "+median)

#create a boxplot of new cases worldwide
plt.title('Worldwide new cases')
plt.ylabel('word_new_case_numbers')
plt.xlabel('date')
plt.boxplot(world_new_cases,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=False,
            showmeans=True,
            showbox=True,
            showcaps=True,
            showfliers=True,
            )
plt.show()


world_new_deaths=covid_data.loc[data2,"new_deaths"]
#plot both new cases and new deaths worldwide
plt.title('Worldwide new cases and deaths')
plt.xlabel('world_dates')
plt.ylabel('world_new_deaths')
plt.boxplot(world_new_deaths,
             vert = True,
             whis = 1.5,
             patch_artist = True,
             meanline = False,
             showbox = True,
             showcaps = True,
             showfliers = True,
             )
plt.show()

# the code to answer my question: How have new cases and total cases developed over time in Spain?
data3 = []
for i in range (0,7996):
     if covid_data.iloc[i,1]=="Spain":
         #choose data in covid_data with "location" showing "Spain"
             data3.append(True)
     else:
             data3.append(False)
Spain_new_cases=covid_data.loc[data3,"new_cases"]

data4 = []
for i in range (0,7996):
     if covid_data.iloc[i,1]=="Spain":
         #choose data in covid_data with "location" showing "Spain"
             data4.append(True)
     else:
             data4.append(False)
Spain_total_cases=covid_data.loc[data3,"total_cases"]

world_dates = []
for i in range (0,7996):
    if covid_data.loc[i, 'location'] == 'World':
        world_dates.append(covid_data.iloc[i, 0])
print(world_dates)

#plot the new cases in Spain
plt.plot(world_dates,Spain_new_cases, 'bo', label = "Spain new cases")
#label the x and y axes and title 
plt.xlabel('world_dates')
plt.ylabel('Spain_new_cases')
plt.title('Spain new cases')
plt.legend()
plt.show()

#plot the total cases in Spain
plt.plot(world_dates,Spain_total_cases, 'bo', label = "Spain total cases")
#label the x and y axes and title
plt.xlabel('world_dates')
plt.ylabel('Spain_total_cases')
plt.title('Spain total cases')
plt.legend()
plt.show()
