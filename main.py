import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import quad # модуль для интегрирования
import scipy.fftpack
import numpy.fft 
import numpy as np
import pylab# модуль построения поверхности
from mpl_toolkits.mplot3d import Axes3D# модуль построения поверхности


f_s = 1000  # Sampling rate, or number of measurements per second

def main():
    # Чтение данных из csv
    fixed_df = pd.read_csv("123.csv", header=None)

    # Преобразование данных в числа
    x = fixed_df[0].values.tolist()
    y = fixed_df[1].values.tolist()
    x = list(map(float, x))
    y = list(map(float, y))

    # построение оригинала
    plt.title("Оригинальные данные")
    plt.plot(x, y, label="data")
    plt.grid(True)
    plt.xlabel("Время t")
    plt.ylabel("Амплитуда В")
    plt.show()

    # построение преобразования
    y_fft = scipy.fftpack.fft(y)
    plt.title("БПФ")
    plt.plot(y_fft, label="data")
    plt.grid(True)
    plt.xlabel("Время t")
    plt.ylabel("f(t),F(t)")
    plt.show()
    

    # построение спектра частот
    freqs = scipy.fftpack.fftfreq(len(x)) * f_s
    plt.title("Спектр частот")
    plt.plot(freqs, y_fft, label="data")
    plt.grid(True)
    plt.xlabel("частота")
    plt.ylabel("величина спектра")
    plt.show()



if __name__ == '__main__':
    main()