from __future__ import division
from math import pi
import numpy as np
import random
# import matplotlib.pyplot as plt

class SineOsc:

    def __init__(self):
        self.sample_rate = 44100

    def wave(self, frequency, length, rate):
        """produces sine across np array"""

        length = int(length * rate)

        factor = float(frequency) * (pi * 2) / rate
        factor2 = float(frequency * 2) * (pi * 2) / rate
        factor3 = float(frequency * 4) * (pi * 2) / rate

        waveform = np.sin(np.arange(length) * factor)
        waveform2 = np.sin(np.arange(length) * factor2)
        waveform3 = np.sin(np.arange(length) * factor3)

        # waveform3 = np.power(waveform, 4)
        rounded_waveform = np.round(waveform2, 0) / 10
        rounded_waveform2 = np.round(waveform3, 0) / 10

        # return np.add(waveform, np.add(rounded_waveform, rounded_waveform2))

        return waveform

    def play(self, stream, length, volume, attack, decay, *freqs):
        """Plays a group of frequencies"""
        all_tones = []
        volume = volume

        for freq in freqs:
            wave = [self.wave(freq, length, self.sample_rate)]
            waveform = (np.concatenate(wave) * volume / 16)

            fade_in = np.arange(0., 1., 1./attack)
            fade_out = np.arange(1., 0., -1./decay)

            waveform[:attack] = np.multiply(waveform[:attack], fade_in)
            waveform[-decay:] = np.multiply(waveform[-decay:], fade_out)

            all_tones.append(waveform)

        all_tones = sum(all_tones)

        # plt.plot(chunk[])
        # plt.show()

        return stream.write(all_tones.astype(np.float32).tostring())
