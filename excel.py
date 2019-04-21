
# coding: utf-8

import matplotlib.pyplot as plt
from scipy.integrate import quad # модуль для интегрирования
import scipy.fftpack
import numpy.fft 
import numpy as np

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

import pylab
import scipy.fftpack
import scipy
import csv
import sys


def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
             for i in range(wanted_parts) ]


def visData(x, y):

    f = scipy.linspace(x[0], x[-1], num=len(x))

    signal = y
    fft = abs(scipy.fft(signal))
    fft_freq = scipy.fftpack.fftfreq(len(signal), f[1] - f[0])

    pylab.subplot(211)
    pylab.plot(x, signal)
    pylab.subplot(212)
    # pylab.vlines(abs(fft_freq), 0, fft, colors='b')
    # pylab.plot(fft, colors='b')
    pylab.plot(abs(fft))
    pylab.show()



def main():
    df = pd.read_excel("ТИМЧЕНКО(син).xls", sheetname="Лист1", header=None)

    x = df[0].values.tolist()
    y = df[1].values.tolist()
    x = list(map(float, x))
    y = list(map(float, y))

    print(len(x))
    print(len(y))

    print("Считано {} значений".format(len(y)))

    visData(x, y)

    start = int(input("Введите начальный индекс последовательности - (от 0 до {}) - ".format(len(y))))
    end = int(input("Введите конечный индекс последовательности - (от 0 до {}) - ".format(len(y))))

    visData(x[start:end], y[start:end])

if __name__ == '__main__':
    main()