
from scipy import fftpack
import numpy as np
import matplotlib.pyplot as plt
from skimage import io

N = 10

def main():

    x = np.zeros(500)
    x[100:150] = 1

    X = fftpack.fft(x)

    f, (ax0, ax1) = plt.subplots(2, 1, sharex=True)

    ax0.plot(x)
    ax0.set_ylim(-0.1, 1.1)

    ax1.plot(fftpack.fftshift(np.abs(X)))
    ax1.set_ylim(-5, 55);
    plt.show()

    t = np.linspace(0, 1, 500)
    x = np.sin(10 * np.pi * t)

    X = fftpack.fft(x)

    f, (ax0, ax1) = plt.subplots(2, 1)

    ax0.plot(x)
    ax0.set_ylim(-1.1, 1.1)

    ax1.plot(fftpack.fftfreq(len(t)), np.abs(X))
    ax1.set_ylim(0, 190);
    plt.show()

    f, ax = plt.subplots()

    N = 10
    beta_max = 5
    colormap = plt.cm.plasma

    norm = plt.Normalize(vmin=0, vmax=beta_max)

    lines = [
        ax.plot(np.kaiser(100, beta), color=colormap(norm(beta)))
        for beta in np.linspace(0, beta_max, N)
        ]

    sm = plt.cm.ScalarMappable(cmap=colormap, norm=norm)

    sm._A = []

    plt.colorbar(sm).set_label(r'Kaiser $\beta$');
    plt.show()

    win = np.kaiser(len(t), 5)
    X_win = fftpack.fft(x * win)

    plt.plot(fftpack.fftfreq(len(t)), np.abs(X_win))
    plt.ylim(0, 190);
    plt.show()

    

if __name__ == "__main__":
    main()



