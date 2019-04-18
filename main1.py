import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import matplotlib.pyplot as plt
from scipy.integrate import quad # модуль для интегрирования
import scipy.fftpack
import numpy.fft 
import numpy as np
import matplotlib.gridspec as gridspec


f_s = 1  # Sampling rate, or number of measurements per second

def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
             for i in range(wanted_parts) ]


def visData(newListX, newListY, i=-1):

    egrid = (2,2)

    fig = plt.figure()

    ax1 = plt.subplot2grid(egrid, (0, 0), colspan=4)
    ax1.plot(newListX, newListY, label="data", color="black")
    ax1.set_xlabel("Время t")
    ax1.set_ylabel("Амплитуда В")
    ax1.grid(True)

    ax2 = plt.subplot2grid(egrid, (1, 0), rowspan=1)
    y_fft = scipy.fftpack.fft(newListY)
    ax2.set_title("БПФ участка {}".format(i+1))

    N = int(len(y_fft)/2+1)

    ax2.plot(np.abs(y_fft[:N]), label="data",color="orange")

    ax2.set_xlabel("Амплитуда")
    ax2.set_ylabel("f(t),F(t)")
    ax2.grid(True)

    ax3 = plt.subplot2grid(egrid, (1, 1), rowspan=1)
    freqs = scipy.fftpack.fftfreq(len(newListX)) * f_s
    ax3.set_title("Спектр частот участка {}".format(i+1))
    ax3.plot(freqs, y_fft, label="data", color="blue")
    ax3.set_xlabel("частота")
    ax3.set_ylabel("величина спектра")
    ax3.grid(True)

    if i == -1:
        ax1.set_title("Оригинальные данные")
        ax2.set_title("БПФ считанных данных")
        ax3.set_title("Спектр частот считанных данных")
    else:
        ax1.set_title("Оригинальные данные участка {}".format(i+1))
        ax2.set_title("БПФ участка {}".format(i+1))
        ax3.set_title("Спектр частот участка {}".format(i+1))

    plt.tight_layout()
    plt.show()


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

    visData(x, y)

    print("Считано {} строк".format(len(y)))
    delimeter = int(input("Введите делитель диапазона (2,3,4...) - "))

    newListX = split_list(x, delimeter)
    newListY = split_list(y, delimeter)


    for i in range(0, len(newListY)):
        visData(newListX[i], newListY[i], i)




if __name__ == '__main__':
    main()