import numpy as np
import matplotlib.pyplot as plt
labels ='USA','India','Brazil','Russia','UK'
fraces = [29862124,11285561,11205972,4360823,4234924]
plt.axes(aspect=1)
plt.pie(x=fraces,labels= labels,autopct='%0f%%')
plt.title('the proportion of infections from the top five most affected countries')
plt.show()
ls=[9410,394141,4442,105338,19149,76779,126550,36269,842,15981]
print(ls)
import matplotlib.pyplot as plt
data = [51,1142,42,216,25,650,32533,57,1,523]
plt.boxplot(x = data)
plt.ylim(0,2000)
plt.show()

