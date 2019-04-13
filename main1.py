import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import matplotlib.pyplot as plt
from scipy.integrate import quad # модуль для интегрирования
import scipy.fftpack
import numpy.fft 
import numpy as np


f_s = 1  # Sampling rate, or number of measurements per second

def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
             for i in range(wanted_parts) ]

def main():
    # Чтение данных из csv
    df = pd.read_excel("ddd.xls", sheetname="scope_7_1", header=None)

    # Преобразование данных в числа
    x = df[0].values.tolist()
    y = df[1].values.tolist()
    x = list(map(float, x))
    y = list(map(float, y))

    delta = x[0]
    x = list(map(lambda z: z+abs(delta), x))

    # построение оригинала
    plt.title("Оригинальные данные")
    plt.plot(x, y, label="data")
    plt.grid(True)
    plt.xlabel("Время t")
    plt.ylabel("Амплитуда В")
    plt.show()

    print("Считано {} строк".format(len(y)))
    delimeter = int(input("Введите делитель диапазона (2,3,4...) - "))

    newListX = split_list(x, delimeter)
    newListY = split_list(y, delimeter)

    for i in range(0, len(newListY)):

        fig = plt.figure()
        ax1 = fig.add_subplot(3,1,1)
        ax1.set_title("Оригинальные данные участка {}".format(i+1))
        ax1.plot(newListX[i], newListY[i], label="data")
        ax1.set_xlabel("Время t")
        ax1.set_ylabel("Амплитуда В")
        ax1.grid(True)

        ax2 = fig.add_subplot(3,1,2)
        y_fft = scipy.fftpack.fft(newListY[i])
        ax2.set_title("БПФ участка {}".format(i+1))
        ax2.plot(y_fft, label="data")
        ax2.set_xlabel("Время t")
        ax2.set_ylabel("f(t),F(t)")
        ax2.grid(True)

        ax3 = fig.add_subplot(3,1,3)
        freqs = scipy.fftpack.fftfreq(len(newListX[i])) * f_s
        ax3.set_title("Спектр частот участка {}".format(i+1))
        ax3.plot(freqs, y_fft, label="data")
        ax3.set_xlabel("частота")
        ax3.set_ylabel("величина спектра")
        ax3.grid(True)

        plt.tight_layout()

        plt.show()



if __name__ == '__main__':
    main()