import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams.update({'font.size':30})
matplotlib.rcParams['figure.figsize'] = 18, 10

data1 = []
data2 = []
data3 = []

files = ['000000001.txt', '000001.txt', '001.txt', '01.txt', '10.txt', '1.txt']

for f in files:
    d = np.loadtxt(f, usecols=0)
    d1 = np.loadtxt(f, usecols=1)
    d2 = np.loadtxt(f, usecols=2)
    data1.append(d)
    data2.append(d1)
    data3.append(d2)

data1 = np.mean(data1, axis=1)
data2 = np.mean(data2, axis=1)
data3 = np.mean(data3, axis=1)
print data1

plt.plot(data1, linewidth = '4', marker = '*', markersize = 14, label='Desktop')
plt.plot(data2, linewidth = '4', marker = '*', markersize = 14, label='Desktop')
plt.plot(data3, linewidth = '4', marker = '*', markersize = 14, label='Desktop')

plt.xlabel('Integration Time')
plt.ylabel('Detection Ratio')

#plt.xticks('1ns', '1us', '1ms', '100ms', '10ms', '1s')

#plt.legend(loc='lower right')

plt.savefig('integration_versus_detection_ratio.pdf')

plt.show()
