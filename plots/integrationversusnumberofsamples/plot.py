import os
import numpy as np
import matplotlib.pyplot as plt

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

print data1
print data2
