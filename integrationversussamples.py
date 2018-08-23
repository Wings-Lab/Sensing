import os
import numpy as np

k = 1
for i in range(10):
    for j in range(50):
        os.system('./rtl_power_fftw -b 8 -e 2 -f 915.8e6 -q -g 1 -t '+str(k)+'s | grep -c \'#\' >>data_odroid/'+str(i)+'.txt')
    k = k/10.0
