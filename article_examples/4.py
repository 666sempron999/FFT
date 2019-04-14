
from scipy import fftpack
import numpy as np

N = 10

def main():
    fftpack.fft(np.ones(N))  # The first component is np.mean(x) * N
    z = np.ones(10)
    z[::2] = -1

    print("Applying FFT to {}".format(z))
    fftpack.fft(z)
    x = np.array([1, 5, 12, 7, 3, 0, 4, 3, 2, 8])
    X = fftpack.fft(x)

    np.set_printoptions(precision=2)

    print("Real part:     ", X.real)
    print("Imaginary part:", X.imag)

    np.set_printoptions()
    fftpack.fftfreq(10)



if __name__ == "__main__":
    main()



