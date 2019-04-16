
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

    ## The above code is equivalent to:
    #
    # v0 = np.cos(2 * pi * fd[0] * t)
    # v1 = np.cos(2 * pi * fd[1] * t + pi / 2)
    # v2 = np.cos(2 * pi * fd[2] * t + pi / 3)
    # v3 = np.cos(2 * pi * fd[3] * t + pi / 5)
    # v4 = np.cos(2 * pi * fd[4] * t + pi / 6)
    #
    ## Blend them together
    # v_single = v0
    # v_sim = (0.33 * v0) + (0.2 * v1) + (0.9 * v2) + (0.02 * v3) + (0.1 * v4)

    data = np.load('radar_scan_0.npz')

    # Load variable 'scan' from 'radar_scan_0.npz'
    scan = data['scan']

    # The dataset contains multiple measurements, each taken with the
    # radar pointing in a different direction.  Here we take one such as
    # measurement, at a specified azimuth (left-right position) and elevation
    # (up-down position).  The measurement has shape (2048,).

    v_actual = scan['samples'][5, 14, :]

    # The signal amplitude ranges from -2.5V to +2.5V.  The 14-bit
    # analogue-to-digital converter in the radar gives out integers
    # between -8192 to 8192.  We convert back to voltage by multiplying by
    # $(2.5 / 8192)$.

    v_actual = v_actual * (2.5 / 8192)
    azimuths = scan['position']['az']  # Get all azimuth measurements
    fig, axes = plt.subplots(3, 1, sharex=True, figsize=(4.8, 2.4))

    # Take FFTs of our signals.  Note the convention to name FFTs with a
    # capital letter.

    V_single = np.fft.fft(v_single)
    V_sim = np.fft.fft(v_sim)
    V_actual = np.fft.fft(v_actual)

    N = len(V_single)

    # with plt.style.context('style/thinner.mplstyle'):
    axes[0].plot(np.abs(V_single[:N // 2]))
    # axes[0].set_ylabel("$|V_\mathrm{single}|$")
    axes[0].set_xlim(0, N // 2)
    axes[0].set_ylim(0, 1100)

    axes[1].plot(np.abs(V_sim[:N // 2]))
    # axes[1].set_ylabel("$|V_\mathrm{sim} |$")
    axes[1].set_ylim(0, 1000)

    axes[2].plot(np.abs(V_actual[:N // 2]))
    axes[2].set_ylim(0, 750)
    # axes[2].set_ylabel("$|V_\mathrm{actual}|$")

    axes[2].set_xlabel("FFT component $n$")

    for ax in axes:
        ax.grid()

    plt.show()
    

if __name__ == "__main__":
    main()



