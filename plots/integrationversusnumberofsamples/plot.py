import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams.update({'font.size':36})
matplotlib.rcParams['figure.figsize'] = 20, 10

data1 = []

for i in range(10):
    data1.append(np.loadtxt('desktop/'+str(i)+'.txt'))
data1 = np.mean(data1, axis=1)
data1 = data1/5

data2 = []

for i in range(10):
    data2.append(np.loadtxt('odroid/tmp10e'+str(i)))

for i in data2:
    print len(i)

data2 = np.mean(data2, axis=1)
data2 = data2/5

plt.plot(data1, linewidth = '4', marker = '*', markersize = 14, label='Desktop')
plt.plot(data2, linewidth = '4', marker = '^', markersize = 14, label='Odroid')

plt.xlabel('Integration Time (10^-x)')
plt.ylabel('#Samples Received')

plt.legend(loc='lower right')

plt.show()
