import pygame.mixer as mixer

class QMixer():
    def __init__(self):
        mixer.init()

    def __del__(self):
        mixer.quit()
   
    def play(fname):
        snd = mixer.Sound(fname)
        snd.play()
