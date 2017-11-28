from __future__ import division

import random
from fractions import Fraction
from random import shuffle
import pyaudio

from clear_osc import SineOsc

osc = SineOsc()

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                output=1,
                )

def check_for_relationship(frequency1, frequency2, relationship, length):
    """Checks for given ratio."""
    # https://en.wikipedia.org/wiki/List_of_intervals_in_5-limit_just_intonation

    print (frequency1, frequency2, Fraction(relationship))
    if round((frequency1/frequency2), 3) == relationship or round((frequency2/frequency1), 3) == relationship:
        osc.play_frequencies(
            stream,
            length,
            .8,
            3000,
            3000,
            frequency1,
            frequency2,
            # frequency1 + frequency2 #uncomment to hear summation tone
        )

def generate_test_array():
    """"Randomized test array"""
    freqs = []
    for frequency1 in range(200, 600):
        for frequency2 in range(200, 600):
            freqs.append((frequency1, frequency2))
    shuffle(freqs)
    return freqs

if __name__ == '__main__':
    test_freqs = generate_test_array()

    for frequency1, frequency2 in test_freqs:
        # check_for_relationship(frequency1, frequency2, (2/1), 3) # Octave
        check_for_relationship(frequency1, frequency2, (3/2), 3) # Perfect Fifth
        # check_for_relationship(frequency1, frequency2, (4/3), 4) # Perfect Fourth
        # check_for_relationship(frequency1, frequency2, (9/8), 3) # Major Second
        #
        check_for_relationship(frequency1, frequency2, (5/4), 3) # Major Third
        # check_for_relationship(frequency1, frequency2, (6/5), 3) # Minor Third
        # check_for_relationship(frequency1, frequency2, (15/8), 3) # Major Seventh
        #
        # check_for_relationship(frequency1, frequency2, (11/8), 3) # 11/8 'in-tune' tritone
