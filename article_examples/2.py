
from scipy import fftpack
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from skimage import util
from scipy import signal


def main():
    rate, audio = wavfile.read('Nightingale-sound.wav')
    audio = np.mean(audio, axis=1)
    N = audio.shape[0]
    L = N / rate

    # print(f'Audio length: {L:.2f} seconds')

    f, ax = plt.subplots()
    ax.plot(np.arange(N) / rate, audio)
    ax.set_xlabel('Time [s]')
    ax.set_ylabel('Amplitude [unknown]');

    plt.grid()
    plt.savefig("figure.png")
    plt.show()

    M = 1024
    slices = util.view_as_windows(audio, window_shape=(M,), step=100)
    win = np.hanning(M + 1)[:-1]
    slices = slices * win
    slices = slices.T
    print('Shape of `slices`:', slices.shape)
    spectrum = np.fft.fft(slices, axis=0)[:M // 2 + 1:-1]
    spectrum = np.abs(spectrum)

    f, ax = plt.subplots(figsize=(4.8, 2.4))

    S = np.abs(spectrum)
    S = 20 * np.log10(S / np.max(S))

    ax.imshow(S, origin='lower', cmap='viridis',
              extent=(0, L, 0, rate / 2 / 1000))
    ax.axis('tight')
    ax.set_ylabel('Frequency [kHz]')
    ax.set_xlabel('Time [s]');
    plt.show()


    freqs, times, Sx = signal.spectrogram(audio, fs=rate, window='hanning',
                                          nperseg=1024, noverlap=M - 100,
                                          detrend=False, scaling='spectrum')

    f, ax = plt.subplots(figsize=(4.8, 2.4))
    ax.pcolormesh(times, freqs / 1000, 10 * np.log10(Sx), cmap='viridis')
    ax.set_ylabel('Frequency [kHz]')
    ax.set_xlabel('Time [s]');
    plt.show()



if __name__ == "__main__":
    main()



