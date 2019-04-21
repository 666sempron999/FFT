
# coding: utf-8

import matplotlib.pyplot as plt
from scipy.integrate import quad # модуль для интегрирования
import scipy.fftpack
import numpy.fft 
import numpy as np

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
 
df = pd.read_excel("ТИМЧЕНКО(син).xls", sheetname="Лист1", header=None)

x = df[0].values.tolist()
y = df[1].values.tolist()
x = list(map(float, x))
y = list(map(float, y))


delta = x[0]

newX = list(map(lambda z: z+abs(delta), x))






x = newX
print(len(x))
print(len(y))



def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
             for i in range(wanted_parts) ]



plt.title("Оригинальные данные")
plt.plot(x, y, label="data")
plt.grid(True)
plt.xlabel("Время t")
plt.ylabel("Амплитуда В")
plt.show()

print("Считано {} строк".format(len(y)))
# delimeter = int(input("Введите делитель диапазона (2,3,4...) - "))

# newListX = split_list(x, delimeter)
# newListY = split_list(y, delimeter)

Y = np.fft.fft(y)




plt.plot(np.abs(Y))


plt.show()


# f_s = 1  # Sampling rate, or number of measurements per second
# for i in range(0, len(newListY)):

#         # # построение оригинала
#         # plt.title("Оригинальные данные участка {}".format(i+1))
#         # plt.plot(newListX[i], newListY[i], label="data")
#         # plt.grid(True)
#         # plt.xlabel("Время t")
#         # plt.ylabel("Амплитуда В")
#         # plt.show()

#         # # построение преобразования
#         # y_fft = scipy.fftpack.fft(newListY[i])
#         # plt.title("БПФ участка {}".format(i+1))
#         # plt.plot(y_fft, label="data")
#         # plt.grid(True)
#         # plt.xlabel("Время t")
#         # plt.ylabel("f(t),F(t)")
#         # plt.show()
        

#         # # построение спектра частот
#         # freqs = scipy.fftpack.fftfreq(len(newListX[i])) * f_s
#         # plt.title("Спектр частот участка {}".format(i+1))
#         # plt.plot(freqs, y_fft, label="data")
#         # plt.grid(True)
#         # plt.xlabel("частота")
#         # plt.ylabel("величина спектра")

#         fig = plt.figure()
#         ax1 = fig.add_subplot(3,1,1)
#         ax1.set_title("Оригинальные данные участка {}".format(i+1))
#         ax1.plot(newListX[i], newListY[i], label="data")
#         ax1.set_xlabel("Время t")
#         ax1.set_ylabel("Амплитуда В")
#         ax1.grid(True)

#         ax2 = fig.add_subplot(3,1,2)
#         y_fft = scipy.fftpack.fft(newListY[i])
#         ax2.set_title("БПФ участка {}".format(i+1))
#         ax2.plot(y_fft, label="data")
#         ax2.set_xlabel("Время t")
#         ax2.set_ylabel("f(t),F(t)")
#         ax2.grid(True)

#         ax3 = fig.add_subplot(3,1,3)
#         freqs = scipy.fftpack.fftfreq(len(newListX[i])) * f_s
#         ax3.set_title("Спектр частот участка {}".format(i+1))
#         ax3.plot(freqs, y_fft, label="data")
#         ax3.set_xlabel("частота")
#         ax3.set_ylabel("величина спектра")
#         ax3.grid(True)

#         plt.tight_layout()

#         plt.show()

