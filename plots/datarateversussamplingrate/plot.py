import os
import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 4]
y = [2, 4, 8]

ux = [1, 2, 4, 8, 16, 32]
uy = [4, 8, 16, 32, 64, 128]

plt.plot(x, y, marker = '*', markersize = 14, label='RTLSDR')
plt.plot(ux, uy, marker = '^', markersize = 14, label='USRP')

plt.show()
