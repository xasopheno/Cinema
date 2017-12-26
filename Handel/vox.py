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


class Vox:
    def __init__(self):
        print('voice_enters')
        self.root = 160
        self.l = 1.5
        self.v = 1
        self.a = 8000
        self.d = 1000

    def bassi(self):
        print ('bass')
        freq = self.root / 2
        v = self.v * 1
        l = self.l
        a = self.a
        d = self.d

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 2,
                     )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 3/2,
                     )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 5/3,
                     )

        for i in range(2):
            osc.play(s, l, v, a, d,
                     freq * 5/4,
                     )

        osc.play(s, l, v, a, d,
                 freq * 4/3,
                 )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq,
                     )

        osc.play(s, l, v, a, d,
                 freq * 4/3,
                 )

        osc.play(s, l, v, a, d,
                 freq * 9/8,
                 )

        osc.play(s, l, v, a, d,
                 freq,
                 )

        # ____________________________

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 3/2,
                     )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 4/3,
                     )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 5/4,
                     )

        osc.play(s, l, v, a, d,
                 freq * 4/3,
                 )

        osc.play(s, l, v, a, d,
                 freq * 9/8,
                 )

        osc.play(s, l, v, a, d,
                 freq * 3/2,
                 )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq,
                     )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 9/8,
                     )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 5/4,
                     )

        osc.play(s, l, v, a, d,
                 freq * 5/3,
                 )

        osc.play(s, l, v, a, d,
                 freq * 15/8,
                 )

        osc.play(s, l, v, a, d,
                 freq * 2,
                 )

        # ______________________________________


        osc.play(s, l, v, a, d,
                 freq * 4/3,
                 )

        osc.play(s, l, v, a, d,
                 freq * 4/3 * 2,
                 )

        osc.play(s, l, v, a, d,
                 freq * 5/4 * 2,
                 )

        for i in range(2):
            osc.play(s, l, v, a, d,
                     freq * 9/8 * 2,
                     )

        osc.play(s, l, v, a, d,
                 freq * 2,
                 )

        osc.play(s, l, v, a, d,
                 freq * 15/8,
                 )

        osc.play(s, l, v, a, d,
                 freq * 5/4 * 2,
                 )

        osc.play(s, l, v, a, d,
                 freq * 4/3 * 2,
                 )

        # ______________________________________

        osc.play(s, l, v, a, d,
                 freq * 9/8 * 2,
                 )

        osc.play(s, l, v, a, d,
                 freq * 5/4 * 2,
                 )

        osc.play(s, l, v, a, d,
                 freq * 5/4,
                 )

        # ______________________________________

        osc.play(s, l, v, a, d,
                 freq * 4/3,
                 )

        for i in range(2):
            osc.play(s, l, v, a, d,
                     freq * 9/8,
                     )

        # ______________________________________

        osc.play(s, l, v, a, d,
                 freq * 3/2,
                 )

        osc.play(s, l, v, a, d,
                 freq * 2,
                 )

        osc.play(s, l, v, a, d,
                 freq,
                 )

        # ____second to last line__________________

        for i in range(2):
            osc.play(s, l, v, a, d,
                     freq * 3/2,
                     )

        osc.play(s, l, v, a, d,
                 freq * 4/3,
                 )

        # ______________________________

        osc.play(s, l, v, a, d,
                 freq * 4/3 * 2,
                 )

        osc.play(s, l, v, a, d,
                 freq * 5/4 * 2,
                 )

        osc.play(s, l, v, a, d,
                 freq* 9/8 * 2,
                 )

        # ______________________________

        for i in range(2):
            osc.play(s, l, v, a, d,
                     freq * 2,
                     )

        osc.play(s, l, v, a, d,
                 freq * 9/8 * 2,
                 )

        # ______________________________

        osc.play(s, l, v, a, d,
                 freq * 5/4 * 2,
                 )

        for i in range(2):
            osc.play(s, l, v, a, d,
                     freq * 5/4,
                     )

        for i in range(2):
            osc.play(s, l, v, a, d,
                     freq * 4/3,
                     )

        osc.play(s, l, v, a, d,
                 freq * 3/2,
                 )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 5/3,
                     )

        osc.play(s, l, v, a, d,
                 freq * 3/2,
                 )

        osc.play(s, l, v, a, d,
                 freq * 4/3 * 2,
                 )

        osc.play(s, l, v, a, d,
                 freq * 5/4 * 2,
                 )

        osc.play(s, l, v, a, d,
                 freq * 4/3 * 2,
                 )

        osc.play(s, l, v, a, d,
                 freq * 3/2 * 2,
                 )

        osc.play(s, l, v, a, d,
                 freq * 3/2,
                 )

        osc.play(s, l * 5, v, a, d,
                 freq * 5/3,
                 )

        #______last_line___________

        osc.play(s, l, v, a, d,
                 freq * 4/3,
                 )

        osc.play(s, l, v, a, d,
                 freq * 3/2,
                 )

        osc.play(s, l, v, a, d,
                 freq * 3/2 /2,
                 )

        #____________________________
        for i in range(2):
            osc.play(s, l, v, a, d,
                     freq,
                     )

        osc.play(s, l, v, a, d,
                 freq * 9/8,
                 )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 5/4,
                     )

            #____________________________

        for i in range(2):
            osc.play(s, l, v, a, d,
                     freq * 4/3,
                     )

        osc.play(s, l, v, a, d,
                 freq * 3/2,
                 )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 5/3,
                     )

            #______last_line___________

        osc.play(s, l, v, a, d,
                 freq * 15/8,
                 )

        osc.play(s, l, v, a, d,
                 freq * 3/2,
                 )

        osc.play(s, l, v, a, d,
                 freq * 2,
                 )

        osc.play(s, l, v, a, d,
                 freq * 4/3,
                 )

        osc.play(s, l, v, a, d,
                 freq * 3/2,
                 )

        osc.play(s, l, v, a, d,
                 freq * 3/2 /2,
                 )

        osc.play(s, l * 4, v, a, d,
                 freq,
                 )

    def viola(self):
        print ('viola')
        freq = self.root * 2
        v = self.v
        l = self.l
        a = self.a
        d = self.d

        for i in range(6):
            osc.play(s, l, v, a, d,
                     freq * 3/2,
                     )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 5/4,
                     )

        for i in range(2):
            osc.play(s, l, v, a, d,
                     freq * 5/4,
                     )

        osc.play(s, l, v, a, d,
                 freq,
                 )

        osc.play(s, l * 3, v, a, d,
                 freq,
                 )

        # ______________________________________

        osc.play(s, l, v, a, d,
                 freq,
                 )

        osc.play(s, l, v, a, d,
                 freq * 9/8,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 5/4,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 3/2,
                 )

        osc.play(s, l * 2, v, a, d,
                 freq * 3/2,
                 )

        osc.play(s, l, v, a, d,
                 freq * 3/2,
                 )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 15/8,
                     )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 3/2,
                     )

        osc.play(s, l, v, a, d,
                 freq * 4/3,
                 )

        osc.play(s, l, v, a, d,
                 freq * 5/3,
                 )

        osc.play(s, l, v, a, d,
                 freq * 3/2,
                 )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 3/2,
                     )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 4/3,
                     )

        osc.play(s, l * 3, v, a, d,
                 freq * 5/4,
                 )


        osc.play(s, l, v, a, d,
                 freq
                 )

        for i in range(2):
            osc.play(s, l, v, a, d,
                     freq * 3/2
                     )

        osc.play(s, l, v, a, d,
                 freq * 5/3
                 )

        for i in range(2):
            osc.play(s, l, v, a, d,
                     freq * 3/2
                     )

        osc.play(s, l, v, a, d,
                 freq * 4/3
                 )

        osc.play(s, l, v, a, d,
                 freq * 9/8
                 )

        osc.play(s, l, v, a, d,
                 freq * 5/3
                 )

        for i in range(2):
            osc.play(s, l, v, a, d,
                     freq * 15/8
                     )

        osc.play(s, l, v, a, d,
                 freq * 5/3
                 )

        osc.play(s, l, v, a, d,
                 freq * 4/3
                 )

        osc.play(s, l, v, a, d,
                 freq * 15/8 /2
                 )

        osc.play(s, l, v, a, d,
                 freq * 5/4
                 )

        osc.play(s, l, v, a, d,
                 freq
                 )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 9/8
                     )

        osc.play(s, l, v, a, d,
                 freq * 2
                 )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 3/2
                     )

        osc.play(s, l, v, a, d,
                 freq * 9/8
                 )

        osc.play(s, l, v, a, d,
                 freq * 15/8
                 )

        osc.play(s, l, v, a, d,
                 freq * 2
                 )

        osc.play(s, l, v, a, d,
                 freq * 5/4 * 2
                 )

        osc.play(s, l, v, a, d,
                 freq * 3/2
                 )

        osc.play(s, l, v, a, d,
                 freq * 2
                 )

        osc.play(s, l, v, a, d,
                 freq * 15/8
                 )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 5/4 * 2
                     )

        for i in range(2):
            osc.play(s, l, v, a, d,
                     freq * 2
                     )

        osc.play(s, l, v, a, d,
                 freq * 15/8
                 )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 5/3
                     )

        for i in range(2):
            osc.play(s, l, v, a, d,
                     freq * 15/8
                     )

        osc.play(s, l, v, a, d,
                 freq * 2
                 )

        osc.play(s, l, v, a, d,
                 freq * 5/3
                 )

        osc.play(s, l * 1.5, v, a, d,
                 freq * 9/8 * 2
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 9/8 * 2
                 )

        osc.play(s, l * 5, v, a, d,
                 freq * 2
                 )

        #     ___________________

        osc.play(s, l, v, a, d,
                 freq * 2
                 )

        osc.play(s, l, v, a, d,
                 freq * 3/2
                 )

        osc.play(s, l, v, a, d,
                 freq * 9/8
                 )

        osc.play(s, l * 3, v, a, d,
                 freq * 5/4
                 )

        for i in range(5):
            osc.play(s, l, v, a, d,
                     freq * 2
                     )

        osc.play(s, l, v, a, d,
                 freq * 15/8
                 )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 5/3
                     )

        osc.play(s, l, v, a, d,
                 freq * 3/2
                 )

        osc.play(s, l, v, a, d,
                 freq * 15/8
                 )

        osc.play(s, l, v, a, d,
                 freq
                 )

        osc.play(s, l, v, a, d,
                 freq * 5/3
                 )

        osc.play(s, l, v, a, d,
                 freq * 9/8
                 )

        osc.play(s, l, v, a, d,
                 freq * 3/2
                 )

        osc.play(s, l * 4, v, a, d,
                 freq * 5/4
                 )




    def violino2(self):
        print ('violino2')
        freq = self.root * 2
        v = self.v
        l = self.l
        a = self.a
        d = self.d

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 5 / 4,
                     )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 15 / 8 /2,
                     )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq,
                     )

        for i in range(2):
            osc.play(s, l, v, a, d,
                     freq * 3/2 /2,
                     )

        osc.play(s, l, v, a, d,
                 freq * 4/3 /2,
                 )


        osc.play(s, l * 3, v, a, d,
                 freq * 5/4 /2,
                 )
        # ____________________________________

        for i in range(2):
            osc.play(s, l, v, a, d,
                     freq * 4/3 /2,
                     )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 3/2 /2,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq,
                 )

        osc.play(s, l * 1.5, v, a, d,
                 freq * 15/8 /2,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 5/3 /2,
                 )

        osc.play(s, l, v, a, d,
                 freq * 15/8 /2,
                 )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 9/8,
                     )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq,
                     )

        for i in range(2):
            osc.play(s, l, v, a, d,
                     freq,
                     )

        osc.play(s, l, v, a, d,
                 freq * 15/8 /2,
                 )

        for i in range(2):
            osc.play(s, l, v, a, d,
                     freq,
                     )

        osc.play(s, l * 2, v, a, d,
                 freq,
                 )

        osc.play(s, l, v, a, d,
                 freq * 15/8 /2,
                 )

        osc.play(s, l * 0.75, v, a, d,
                 freq * 5/3 /2,
                 )

        osc.play(s, l * 0.25, v, a, d,
                 freq * 3/2 /2,
                 )

        osc.play(s, l * 3, v, a, d,
                 freq * 3/2 /2,
                 )

        #     ________________________

        osc.play(s, l, v, a, d,
                 freq,
                 )

        osc.play(s, l, v, a, d,
                 freq * 9/8,
                 )

        osc.play(s, l, v, a, d,
                 freq,
                 )

        osc.play(s, l, v, a, d,
                 freq,
                 )

        osc.play(s, l, v, a, d,
                 freq * 15/8 /2,
                 )

        osc.play(s, l, v, a, d,
                 freq,
                 )

        for i in range(2):
            osc.play(s, l, v, a, d,
                     freq * 4/3,
                     )

        osc.play(s, l, v, a, d,
                 freq * 5/4,
                 )

        for i in range(2):
            osc.play(s, l, v, a, d,
                     freq * 9/8,
                     )

        osc.play(s, l * 1.5, v, a, d,
                 freq,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 9/8,
                 )

        osc.play(s, l * 1.5, v, a, d,
                 freq * 15/8 /2,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 5/3 /2,
                 )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 5/3 /2,
                     )

        osc.play(s, l, v, a, d,
                 freq * 15/8 /2,
                 )

        osc.play(s, l, v, a, d,
                 freq * 3/2 /2,
                 )

        osc.play(s, l, v, a, d,
                 freq,
                 )

        #     ______________________

        osc.play(s, l * .75, v, a, d,
                 freq * 15/8 /2,
                 )

        osc.play(s, l * .25, v, a, d,
                 freq * 5/3 /2,
                 )

        for i in range(2):
            osc.play(s, l, v, a, d,
                     freq * 15/8 /2,
                     )

        osc.play(s, l, v, a, d,
                 freq * 9/8,
                 )

        osc.play(s, l, v, a, d,
                 freq * 5/4,
                 )

        osc.play(s, l, v, a, d,
                 freq * 15/8 /2,
                 )

        #     _______________________________

        osc.play(s, l, v, a, d,
                 freq,
                 )

        osc.play(s, l, v, a, d,
                 freq * 5/4,
                 )

        osc.play(s, l, v, a, d,
                 freq * 4/3,
                 )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 3/2,
                     )

        for i in range(2):
            osc.play(s, l, v, a, d,
                     freq * 4/3,
                     )

        osc.play(s, l, v, a, d,
                 freq * 9/8,
                 )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq,
                     )

        for i in range(2):
            osc.play(s, l, v, a, d,
                     freq * 9/8,
                     )

        osc.play(s, l, v, a, d,
                 freq * 5/4,
                 )

        for i in range(2):
            osc.play(s, l, v, a, d,
                     freq,
                     )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 15/8 /2,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 3/2,
                 )

        osc.play(s, l, v, a, d,
                 freq * 3/2,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 4/3,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 5/4,
                 )

        osc.play(s, l * 3, v, a, d,
                 freq * 4/3,
                 )

        #    ________last line________________

        osc.play(s, l, v, a, d,
                 freq * 5/3 /2,
                 )

        osc.play(s, l * 1.5, v, a, d,
                 freq * 15/8/2,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq,
                 )

        osc.play(s, l * 3, v, a, d,
                 freq,
                 )

        #    ________last line________________

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 3/2,
                     )

        for i in range(2):
            osc.play(s, l, v, a, d,
                     freq * 4/3,
                     )

        osc.play(s, l, v, a, d,
                 freq * 9/8,
                 )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq,
                     )

        osc.play(s, l * 1.5, v, a, d,
                 freq * 9/8,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 4/3,
                 )

        osc.play(s, l, v, a, d,
                 freq * 5/4,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 9/8,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq,
                 )

        osc.play(s, l, v, a, d,
                 freq,
                 )

        osc.play(s, l, v, a, d,
                 freq * 15/8 / 2,
                 )

        osc.play(s, l * 4, v, a, d,
                 freq,
                 )


    def violino1(self):
        print ('violino1')
        freq = self.root * 4
        v = self.v * .8
        l = self.l
        a = self.a
        d = self.d

        time.sleep(l * 7.01)

        osc.play(s, l * 3, v, a, d,
                 freq,
                 )

        osc.play(s, l, v, a, d,
                 freq * 15/8 /2,
                 )

        osc.play(s, l * 0.75, v, a, d,
                 freq * 5/3 /2,
                 )

        osc.play(s, l * 0.25, v, a, d,
                 freq * 3/2 /2,
                 )

        osc.play(s, l * 3, v, a, d,
                 freq * 3/2 /2,
                 )

        osc.play(s, l, v, a, d,
                 freq * 5/3 /2,
                 )

        osc.play(s, l, v, a, d,
                 freq * 15/8 /2,
                 )

        osc.play(s, l * 0.25, v, a, d,
                 freq,
                 )

        osc.play(s, l * 0.25, v, a, d,
                 freq * 9/8,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 5/4,
                 )

        osc.play(s, l * 1.5, v, a, d,
                 freq * 9/8,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq,
                 )

        osc.play(s, l, v, a, d,
                 freq * 9/8,
                 )

        for i in range(2):
            osc.play(s, l, v, a, d,
                     freq * 5/3,
                     )

        osc.play(s, l, v, a, d,
                 freq * 15/8,
                 )

        # ______________________________________

        osc.play(s, l * 1.5, v, a, d,
                 freq * 2,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 3/2,
                 )

        osc.play(s, l * 1.5, v, a, d,
                 freq * 3/2,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 5/3,
                 )

        osc.play(s, l * 1.5, v, a, d,
                 freq * 4/3,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 5/4,
                 )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 5/4,
                     )

        for i in range(3):
            osc.play(s, l, v, a, d,
                     freq * 4/3,
                     )

        osc.play(s, l, v, a, d,
                 freq * 3/2,
                 )

        for i in range(2):
            osc.play(s, l, v, a, d,
                     freq,
                     )

        for i in range(2):
            osc.play(s, l, v, a, d,
                     freq * 4/3,
                     )

        osc.play(s, l, v, a, d,
                 freq * 5/4,
                 )

        osc.play(s, l * 1.5, v, a, d,
                 freq * 9/8,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq,
                 )

        osc.play(s, l, v, a, d,
                 freq,
                 )

        for i in range(2):
            osc.play(s, l, v, a, d,
                     freq * 15/8,
                     )

        osc.play(s, l, v, a, d,
                 freq * 5/3,
                 )

        osc.play(s, l * 1.5, v, a, d,
                 freq * 5/3 * 15/8 /2,
                 )

        osc.play(s, l * 0.25, v, a, d,
                 freq * 5/3,
                 )

        osc.play(s, l * 0.25, v, a, d,
                 freq * 5/3 * 15/8 /2,
                 )

        osc.play(s, l, v, a, d,
                 freq * 5/3,
                 )

        for i in range(2):
            osc.play(s, l, v, a, d,
                     freq * 5/3 /2,
                     )

        osc.play(s, l, v, a, d,
                 freq * 5/3 /2 * 15/8 /2,
                 )

        osc.play(s, l, v, a, d,
                 freq * 5/3 /2,
                 )

        osc.play(s, l * 3, v, a, d,
                 freq * 4/3,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 5/4,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 9/8,
                 )

        osc.play(s, l, v, a, d,
                 freq * 5/4,
                 )

        osc.play(s, l * 0.75, v, a, d,
                 freq * 9/8,
                 )

        osc.play(s, l * 0.25, v, a, d,
                 freq,
                 )

        osc.play(s, l, v, a, d,
                 freq * 9/8,
                 )

        osc.play(s, l * 2, v, a, d,
                 freq * 5/3,
                 )

        osc.play(s, l, v, a, d,
                 freq * 3/2,
                 )

        osc.play(s, l * 0.75, v, a, d,
                 freq * 4/3,
                 )

        osc.play(s, l * 0.25, v, a, d,
                 freq * 5/4,
                 )

        osc.play(s, l * 3, v, a, d,
                 freq * 5/4,
                 )

        for i in range(2):
            osc.play(s, l, v, a, d,
                     freq * 2,
                     )

        osc.play(s, l, v, a, d,
                 freq * 15/8,
                 )

        osc.play(s, l * 1.5, v, a, d,
                 freq * 5/3,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 3/2,
                 )

        osc.play(s, l, v, a, d,
                 freq * 3/2,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 3/2,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 9/8 * 5/4
                 )

        osc.play(s, l * 1.5, v, a, d,
                 freq * 9/8 * 5/4
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 9/8 * 5/4
                 )

        osc.play(s, l * 1.5, v, a, d,
                 freq * 3/2,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 5/3,
                 )

        osc.play(s, l, v, a, d,
                 freq * 3/2,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 4/3,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 5/4,
                 )

        osc.play(s, l * 1.5, v, a, d,
                 freq * 9/8,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 15/8,
                 )

        osc.play(s, l * 5, v, a, d,
                 freq * 2,
                 )

        #  ___________________

        osc.play(s, l * 0.25, v, a, d,
                 freq * 9/8,
                 )

        osc.play(s, l * 0.25, v, a, d,
                 freq * 5/4,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 4/3,
                 )

        osc.play(s, l, v, a, d,
                 freq * 5/4,
                 )

        osc.play(s, l * 0.75, v, a, d,
                 freq * 9/8,
                 )

        osc.play(s, l * 0.25, v, a, d,
                 freq,
                 )

        osc.play(s, l * 3, v, a, d,
                 freq,
                 )

        #   ____________

        for i in range(2):
            osc.play(s, l, v, a, d,
                     freq * 2,
                     )

        osc.play(s, l, v, a, d,
                 freq * 15/8,
                 )

        osc.play(s, l * 1.5, v, a, d,
                 freq * 5/3,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 3/2,
                 )

        osc.play(s, l, v, a, d,
                 freq * 3/2,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 3/2,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 9/8 * 5/4
                 )

        osc.play(s, l * 1.5, v, a, d,
                 freq * 9/8 * 5/4
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 9/8 * 5/4
                 )

        osc.play(s, l * 1.5, v, a, d,
                 freq * 3/2,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 5/3,
                 )

        osc.play(s, l, v, a, d,
                 freq * 3/2,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 4/3,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq * 5/4,
                 )

        osc.play(s, l * 1.5, v, a, d,
                 freq * 9/8,
                 )

        osc.play(s, l * 0.5, v, a, d,
                 freq,
                 )

        osc.play(s, l * 4, v, a, d,
                 freq,
                 )
