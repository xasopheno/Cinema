import random
import pyaudio
from clear_osc import SineOsc
import multiprocessing as mp
import time
from opening import Opening
from vox import Vox

osc = SineOsc()

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                output=1,
                )

def play_opening():
    opening = Opening()

    p1 = mp.Process(target=opening.bassi)
    p1.start()
    p2 = mp.Process(target=opening.viola)
    p2.start()
    p3 = mp.Process(target=opening.violino2)
    p3.start()
    p4 = mp.Process(target=opening.violino1)
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()


def voice_enters():
    vox = Vox()
    p1 = mp.Process(target=vox.bassi)
    p1.start()
    p2 = mp.Process(target=vox.viola)
    p2.start()
    p3 = mp.Process(target=vox.violino2)
    p3.start()
    p4 = mp.Process(target=vox.violino1)
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()


if __name__=='__main__':
    mp.set_start_method('spawn')
    play_opening()
    voice_enters()
