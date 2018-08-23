import os
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

matplotlib.rcParams.update({'font.size':30})
matplotlib.rcParams['figure.figsize'] = 18, 10

x = [1, 2, 4]
y = [2, 4, 8]

ux = [1, 2, 4, 8, 16, 24, 32]
uy = [4, 8, 16, 32, 64, 96, 128]

plt.plot(x, [i*8 for i in y], marker = '*', markersize = 14, label='RTLSDR')
plt.plot(ux, [i*8 for i in uy], marker = '^', markersize = 14, label='USRP')

plt.xlabel('Sample Rate (MHz)')
plt.ylabel('Data Rate (Mbps)')

plt.legend(loc='lower right')

plt.savefig('datarateversussamplingrate.pdf')
plt.show()
