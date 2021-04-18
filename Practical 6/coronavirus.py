#make a frequency dictionary containing the information in the table 
frequency = {'USA':29862124, 'India':11285561, 'Brazil':11205972, 'Russia':4360823, 'UK':4234924}
print(frequency)
import numpy as np
#import matplotlib
import matplotlib.pyplot as plt
#input the names of different countries
labels ='USA','India','Brazil','Russia','UK'
#input the number of cases in different countries
fraces = [29862124,11285561,11205972,4360823,4234924]
plt.axes(aspect=1)
plt.pie(x=fraces,labels= labels,autopct='%0f%%')
#give the figure a title
plt.title('the proportion of infections from the top five most affected countries')
plt.show() 
