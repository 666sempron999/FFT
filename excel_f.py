
# coding: utf-8
import sys
import numpy as np
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import matplotlib.pyplot as plt


def visData(x, y):
    """
    data visualisation with fft
    """

    # plot original data
    plt.title("Оригинальные данные")
    plt.plot(x, y, label="data")
    plt.grid(True)
    plt.xlabel("Время t")
    plt.ylabel("Амплитуда В")
    plt.show()


    fft = np.fft.fft(y)
    # for i in range(2):
    #     print("Value at index {}:\t{}".format(i, fft[i + 1]), "\nValue at index {}:\t{}".format(fft.size -1 - i, fft[-1 - i]))

    T = x[1] - x[0]
    N = len(y)
    f = np.linspace(0, 1 / T, N)

    plt.ylabel("Amplitude")
    plt.xlabel("Frequency [Hz]")

    newX = f[:N // 2]
    newY = np.abs(fft)[:N // 2] * 1 / N
    plt.bar(newX, newY, width=5)  # 1 / N is a normalization factor
    plt.grid()
    plt.show()

    for i in range(0, len(newX)):
        print("{} - {} : {}".format(i, newX[i], newY[i]))
    # for i in enumerate(newX, newY):
    #     print(i)


def split_list(alist, wanted_parts=1):
    """
    method for spliting list99 to euqval parts
    """
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
             for i in range(wanted_parts) ]


def main():

    df = pd.read_excel("scope7_1.xls", sheetname="scope_7_1", header=None)
    x = df[0].values.tolist()
    y = df[1].values.tolist()
    x = list(map(float, x))
    y = list(map(float, y))

    if x[0] < 0:
        delta = abs(x[0])
        x = list(map(lambda xres: xres+delta, x))

    # while True:
    print("Считано {} значений".format(len(y)))

    x1 = int(input("Введите начальное значение - "))
    x2 = int(input("Введите конечное значение - "))

    if (x2 < x1) or (x2 > len(y)) or( x1 > len(y)):
        print("Ошибка при вводе интервала!")
        print("*"*30)
        # continue
        return False

    visData(x[x1:x2], y[x1:x2])
    print("Нажмите Ctrl+z для выхода")

    print("*"*50)

        

if __name__ == '__main__':
    main()