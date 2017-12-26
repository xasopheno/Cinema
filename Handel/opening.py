import random
import pyaudio
from clear_osc import SineOsc
import multiprocessing as mp
import time

osc = SineOsc()

p = pyaudio.PyAudio()
s = p.open(format=pyaudio.paFloat32,
           channels=1,
           rate=44100,
           output=1,
           )


class Opening:
    def __init__(self):
        self.root = 160
        self.l = 1.5
        self.v = 1
        self.a = 8000
        self.d = 1000

    def bassi(self):
        print ('bass')
        freq = self.root /2
        v = self.v
        l = self.l
        a = self.a
        d = self.d
        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq,
                     )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 9 / 8,
                     )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 5 / 4,
                     )


        osc.play(s, l, v, a, d,
                 freq * 4 / 3,
                 )


        osc.play(s, l, v, a, d,
                 freq * 9 / 8,
                 )

        osc.play(s, l, v, a, d,
                 freq,
                 )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 3 / 2,
                     )

        # ______________________________________


        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 4 / 3,
                     )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 5 / 4,
                     )

        v /= 2
        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 9 / 8,
                     )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq,
                     )

        v *= 2
        osc.play(s, l, v, a, d,
                 freq * 2,
                 )

        osc.play(s, l, v, a, d,
                 freq * 2 * 9 / 8,
                 )

        osc.play(s, l, v, a, d,
                 freq * 2 * 5 / 4,
                 )

        osc.play(s, l, v, a, d,
                 freq * 2 * 4 / 3,
                 )

        osc.play(s, l, v, a, d,
                 freq * 4 / 3,
                 )

        osc.play(s, l, v, a, d,
                 freq * 3 / 2,
                 )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 5 / 3,
                     )

        osc.play(s, l, v, a, d,
                 freq * 3 / 2,
                 )

        osc.play(s, l, v, a, d,
                 freq * 15 / 8,
                 )

        osc.play(s, l, v, a, d,
                 freq * 2,
                 )

        osc.play(s, l, v, a, d,
                 freq * 4 / 3,
                 )

        osc.play(s, l, v, a, d,
                 freq * 3 / 2,
                 )

        osc.play(s, l, v, a, d,
                 freq * 3 / 2 / 2,
                 )

        osc.play(s, l * 3, v, a, d,
                 freq,
                 )

    def viola(self):
        print ('viola')
        freq = self.root * 2
        v = self.v
        l = self.l
        a = self.a
        d = self.d

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 5 / 4,
                     )

        for i in range(2):
            osc.play(s, l, v, a, d,
                     freq * 9 / 8,
                     )


        osc.play(s, l, v, a, d,
                 freq * 15 / 8 / 2,
                 )

        osc.play(s, l * 3, v, a, d,
                 freq
                 )


        osc.play(s, l, v, a, d,
                 freq
                 )

        osc.play(s, l, v, a, d,
                 freq * 9 / 8
                 )

        osc.play(s, l * .5, v, a, d,
                 freq * 5 / 4
                 )

        osc.play(s, l * .5, v, a, d,
                 freq * 3 / 2
                 )

        osc.play(s, l * 3, v, a, d,
                 freq * 3 / 2
                 )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 15 / 8
                     )

        osc.play(s, l * 3, v, a, d,
                 freq * 2
                 )

        v /= 2
        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 5 / 3
                     )

        osc.play(s, l * 3, v, a, d,
                 freq * 3 / 2
                 )

        v *= 2
        osc.play(s, l, v, a, d,
                 freq * 3 / 2
                 )

        osc.play(s, l, v, a, d,
                 freq * 4 / 3
                 )

        osc.play(s, l, v, a, d,
                 freq * 2
                 )

        osc.play(s, l * 2, v, a, d,
                 freq * 4 / 3 * 2
                 )


        osc.play(s, l, v, a, d,
                 freq * 5 / 4 * 2
                 )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 5 / 3
                     )


        osc.play(s, l, v, a, d,
                 freq * 15 / 8
                 )

        osc.play(s, l * .75, v, a, d,
                 freq * 3 / 2
                 )

        osc.play(s, l * .25, v, a, d,
                 freq * 4 / 3
                 )

        osc.play(s, l, v, a, d,
                 freq * 5 / 4
                 )

        osc.play(s, l, v, a, d,
                 freq * 5 / 3
                 )

        osc.play(s, l, v, a, d,
                 freq * 9 / 8
                 )

        osc.play(s, l, v, a, d,
                 freq * 3 / 2
                 )

        osc.play(s, l * 3, v, a, d,
                 freq * 5 / 4
                 )
    # ______________________________________


    def violino2(self):
        print ('violino2')
        freq = self.root * 2
        v = self.v
        l = self.l
        a = self.a
        d = self.d
        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 3 / 2,
                     )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 4 / 3,
                     )

        osc.play(s, l * 3, v, a, d,
                 freq * 5 / 4,
                 )


        osc.play(s, l, v, a, d,
                 freq * 5 / 3,
                 )


        osc.play(s, l, v, a, d,
                 freq * 4 / 3,
                 )

        osc.play(s, l / 2, v, a, d,
                 freq * 3 / 2,
                 )


        osc.play(s, l / 2, v, a, d,
                 freq * 2,
                 )

        osc.play(s, l * 3, v, a, d,
                 freq * 15 / 8,
                 )

        # ______________________________________

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 9 / 8,
                     )

        osc.play(s, l * 3, v, a, d,
                 freq * 5 / 4,
                 )

        v /= 2
        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 15 / 8 / 2,
                     )

        osc.play(s, l * 3, v, a, d,
                 freq,
                 )

        v *= 2
        osc.play(s, l, v, a, d,
                 freq * 5 / 4
                 )

        osc.play(s, l, v, a, d,
                 freq * 4 / 3
                 )

        osc.play(s, l, v, a, d,
                 freq * 3 / 2
                 )

        osc.play(s, l * 2, v, a, d,
                 freq
                 )

        osc.play(s, l, v, a, d,
                 freq * 15 / 8 / 2
                 )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq
                     )

        osc.play(s, l * 2, v, a, d,
                 freq * 9 / 8
                 )

        osc.play(s, l, v, a, d,
                 freq
                 )

        osc.play(s, l * 2, v, a, d,
                 freq
                 )

        osc.play(s, l, v, a, d,
                 freq * 15 / 8
                 )

        osc.play(s, l * 3, v, a, d,
                 freq
                 )

    def violino1(self):
        print ('violino1')
        freq = self.root * 4
        v = self.v * .8
        l = self.l
        a = self.a
        d = self.d
        osc.play(s, l * 4, v, a, d,
                 freq,
                 )

        osc.play(s, l, v, a, d,
                 freq * 15 / 8 / 2,
                 )


        osc.play(s, l * .75, v, a, d,
                 freq * 5 / 3 / 2,
                 )

        osc.play(s, l * .25, v, a, d,
                 freq * 3 / 2 / 2,
                 )

        osc.play(s, l * 3, v, a, d,
                 freq * 3 / 2 / 2,
                 )


        osc.play(s, l, v, a, d,
                 freq * 5 / 3 / 2,
                 )

        osc.play(s, l, v, a, d,
                 freq * 15 / 8 / 2,
                 )

        osc.play(s, l * .25, v, a, d,
                 freq
                 )

        osc.play(s, l * .25, v, a, d,
                 freq * 9 / 8
                 )

        osc.play(s, l * .5, v, a, d,
                 freq * 5 / 4
                 )

        osc.play(s, l * 3, v, a, d,
                 freq * 9 / 8
                 )

        # ______________________________________

        v /= 2
        osc.play(s, l * 3, v, a, d,
                 freq * 5 / 3
                 )

        osc.play(s, l * 3, v, a, d,
                 freq * 3 / 2
                 )

        # time.sleep(1)
        v *= 2
        osc.play(s, l * 3, v, a, d,
                 freq * 4 / 3
                 )


        osc.play(s, l * 3, v, a, d,
                 freq * 5 / 4
                 )

        # time.sleep(1)

        # _____________________________________

        osc.play(s, l, v, a, d,
                 freq * 2
                 )


        osc.play(s, l, v, a, d,
                 freq * 2
                 )


        osc.play(s, l, v, a, d,
                 freq * 15 / 8
                 )

        osc.play(s, l * 1.5, v, a, d,
                 freq * 5 / 3
                 )

        osc.play(s, l * .5, v, a, d,
                 freq * 3 / 2
                 )

        osc.play(s, l * 1.5, v, a, d,
                 freq * 3 / 2
                 )

        for i in range(2):
            osc.play(s, l * .5, v, a, d,
                     freq * 9/8 * 5/4
                     )
            osc.play(s, l * .5, v, a, d,
                     freq * 3 / 2
                     )

        osc.play(s, l * .5, v, a, d,
                 freq * 9/8 * 5/4
                 )

        osc.play(s, l * 3, v, a, d,
                 freq * 3 / 2
                 )

        osc.play(s, l * .5, v, a, d,
                 freq * 4 / 3
                 )

        osc.play(s, l * .5, v, a, d,
                 freq * 5 / 4
                 )

        osc.play(s, l * 1.5, v, a, d,
                 freq * 9 / 8
                 )

        osc.play(s, l * .5, v, a, d,
                 freq
                 )

        osc.play(s, l * 3, v, a, d,
                 freq
                 )
