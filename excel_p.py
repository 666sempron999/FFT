
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

    print("Обработано {} значений".format(len(y)))

    # plot fft data
    plt.title("Первый этап ДПФ")
    t = np.linspace(0, len(x), len(x), endpoint=True)
    Y = np.fft.fft(y)
    plt.plot(Y, label="Данные ДПФ")
    plt.legend()
    plt.grid()
    plt.show()

    # devide data for two euqval parts and plot it
    N = int(len(Y)/2+1)
    plt.title("Второй этап ДПФ")
    plt.plot(np.abs(Y), label="Данные 1")
    plt.plot(np.abs(Y[:N]), label="Данные 2")

    dt = x[1] - x[0]
    fa = 1.0/dt # scan frequency
    print("Частота в считанном массиве данных - {}".format(fa))

    X = np.linspace(0, fa/2, N, endpoint=True)
    plt.xlabel("Частота")
    plt.plot(X, np.abs(Y[:N]), label="Данные 3")

    plt.legend()
    plt.grid()
    plt.show()

    # ploting results
    plt.plot(X, 2.0*np.abs(Y[:N])/N, label="Зависимость амплитуды от частоты")
    plt.title("Результат")
    plt.xlabel('Частота ($Hz$)')
    plt.ylabel('Амплитуда ($Unit$)')
    plt.legend()
    plt.grid()
    plt.show()


def split_list(alist, wanted_parts=1):
    """
    method for spliting list to euqval parts
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

    while True:
        print("Считано {} значений".format(len(y)))

        x1 = int(input("Введите начальное значение - "))
        x2 = int(input("Введите конечное значение - "))

        if (x2 < x1) or (x2 > len(y)) or( x1 > len(y)):
            print("Ошибка при вводе интервала!")
            print("*"*30)
            continue

        visData(x[x1:x2], y[x1:x2])
        print("Нажмите Ctrl+z для выхода")

        print("*"*50)

        

if __name__ == '__main__':
    main()