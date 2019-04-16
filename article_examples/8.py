
from scipy import fftpack
import numpy as np
import matplotlib.pyplot as plt
from skimage import io



def main():

    pi = np.pi

    # Radar parameters
    fs = 78125          # Sampling frequency in Hz, i.e., we sample 78125
                        # times per second

    ts = 1 / fs         # Sampling time, i.e., one sample is taken each
                        # ts seconds

    Teff = 2048.0 * ts  # Total sampling time for 2048 samples
                        # (AKA effective sweep duration) in seconds.

    Beff = 100e6        # Range of transmit signal frequency during the time the
                        # radar samples, known as the "effective bandwidth"
                        # (given in Hz)

    S = Beff / Teff     # Frequency sweep rate in Hz/s

    # Specification of targets.  We made these targets up, imagining they
    # are objects seen by the radar with the specified range and size.

    R = np.array([100, 137, 154, 159,  180])  # Ranges (in meter)
    M = np.array([0.33, 0.2, 0.9, 0.02, 0.1])  # Target size
    P = np.array([0, pi / 2, pi / 3, pi / 5, pi / 6])  # Randomly chosen phase offsets

    t = np.arange(2048) * ts  # Sample times

    fd = 2 * S * R / 3E8      # Frequency differences for these targets

    # Generate five targets
    signals = np.cos(2 * pi * fd * t[:, np.newaxis] + P)

    # Save the signal associated with the first target as an example for
    # later inspection
    v_single = signals[:, 0]

    # Weigh the signals, according to target size and sum, to generate
    # the combined signal seen by the radar.
    v_sim = np.sum(M * signals, axis=1)

    
    plt.show()

    

if __name__ == "__main__":
    main()



