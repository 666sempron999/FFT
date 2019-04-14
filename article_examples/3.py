
from scipy import fftpack
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from skimage import util
from scipy import signal

import time

from scipy import fftpack
from sympy import factorint


def main():
    # rate, audio = wavfile.read('Nightingale-sound.wav')
    # audio = np.mean(audio, axis=1)
    # N = audio.shape[0]
    # L = N / rate

    # # print(f'Audio length: {L:.2f} seconds')

    # f, ax = plt.subplots()
    # ax.plot(np.arange(N) / rate, audio)
    # ax.set_xlabel('Time [s]')
    # ax.set_ylabel('Amplitude [unknown]');

    # plt.grid()
    # plt.savefig("figure.png")
    # plt.show()

    # M = 1024
    # slices = util.view_as_windows(audio, window_shape=(M,), step=100)
    # win = np.hanning(M + 1)[:-1]
    # slices = slices * win
    # slices = slices.T
    # print('Shape of `slices`:', slices.shape)
    # spectrum = np.fft.fft(slices, axis=0)[:M // 2 + 1:-1]
    # spectrum = np.abs(spectrum)

    # f, ax = plt.subplots(figsize=(4.8, 2.4))

    # S = np.abs(spectrum)
    # S = 20 * np.log10(S / np.max(S))

    # ax.imshow(S, origin='lower', cmap='viridis',
    #           extent=(0, L, 0, rate / 2 / 1000))
    # ax.axis('tight')
    # ax.set_ylabel('Frequency [kHz]')
    # ax.set_xlabel('Time [s]');
    # plt.show()


    # freqs, times, Sx = signal.spectrogram(audio, fs=rate, window='hanning',
    #                                       nperseg=1024, noverlap=M - 100,
    #                                       detrend=False, scaling='spectrum')

    # f, ax = plt.subplots(figsize=(4.8, 2.4))
    # ax.pcolormesh(times, freqs / 1000, 10 * np.log10(Sx), cmap='viridis')
    # ax.set_ylabel('Frequency [kHz]')
    # ax.set_xlabel('Time [s]');
    # plt.show()

    K = 1000
    lengths = range(250, 260)

    # Calculate the smoothness for all input lengths
    smoothness = [max(factorint(i).keys()) for i in lengths]


    exec_times = []
    for i in lengths:
        z = np.random.random(i)

        # For each input length i, execute the FFT K times
        # and store the execution time

        times = []
        for k in range(K):
            tic = time.monotonic()
            fftpack.fft(z)
            toc = time.monotonic()
            times.append(toc - tic)

        # For each input length, remember the *minimum* execution time
        exec_times.append(min(times))


    f, (ax0, ax1) = plt.subplots(2, 1, sharex=True)
    ax0.stem(lengths, np.array(exec_times) * 10**6)
    ax0.set_ylabel('Execution time (µs)')

    ax1.stem(lengths, smoothness)
    ax1.set_ylabel('Smoothness of input length\n(lower is better)')
    ax1.set_xlabel('Length of input')
    plt.show()



if __name__ == "__main__":
    main()



