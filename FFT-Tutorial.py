# -*- coding: utf-8 -*-


import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



t = np.linspace(0, 2*np.pi, 1000, endpoint=True)
f = 3.0 # Frequency in Hz
A = 100.0 # Amplitude in Unit
s = A * np.sin(2*np.pi*f*t) # Signal


plt.plot(t,s)
plt.xlabel('Time ($s$)')
plt.ylabel('Amplitude ($Unit$)')
plt.show()


Y = np.fft.fft(s)
plt.plot(Y)
plt.show()

N = int(len(Y)/2+1)


plt.plot(np.abs(Y))
plt.plot(np.abs(Y[:N]))

plt.show()

dt = t[1] - t[0]
fa = 1.0/dt # scan frequency
print('dt=%.5fs (Sample Time)' % dt)
print('fa=%.2fHz (Frequency)' % fa)

X = np.linspace(0, fa/2, N, endpoint=True)


plt.plot(X, np.abs(Y[:N]))
plt.xlabel('Frequency ($Hz$)')

plt.show()


plt.plot(X, 2.0*np.abs(Y[:N])/N)
plt.xlabel('Frequency ($Hz$)')
plt.ylabel('Amplitude ($Unit$)')
plt.show()
