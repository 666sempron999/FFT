import matplotlib.pyplot as plt
import numpy as np

# def DFT(x):
#     """
#     Compute the discrete Fourier Transform of the 1D array x
#     :param x: (array)
#     """

#     N = x.size
#     n = np.arange(N)
#     k = n.reshape((N, 1))
#     e = np.exp(-2j * np.pi * k * n / N)
#     return np.dot(e, x)


def main():
    t = np.linspace(0, 0.5, 500)
    s = np.sin(40 * 2 * np.pi * t) + 0.5 * np.sin(90 * 2 * np.pi * t)

    plt.ylabel("Amplitude")
    plt.xlabel("Time [s]")
    plt.plot(t, s)
    plt.show()

    fft = np.fft.fft(s)


    for i in range(3):
        print("Value at index {}:\t{}".format(i, fft[i + 1]), "\nValue at index {}:\t{}".format(fft.size -1 - i, fft[-1 - i]))


    # fft = np.fft.fft(s)
    T = t[1] - t[0]  # sampling interval 
    N = s.size

    # 1/T = frequency
    f = np.linspace(0, 1 / T, N)

    plt.ylabel("Amplitude")
    plt.xlabel("Frequency [Hz]")
    plt.bar(f[:N // 2], np.abs(fft)[:N // 2] * 1 / N, width=2.5)  # 1 / N is a normalization factor
    plt.show()

if __name__ == '__main__':
    main()