import numpy as np
import time

class Fasor():
    def __init__(self, sinal):
        self.frequencia = 60
        self.amostragem = 128
        self.sinal = sinal
        self.cria_referencia()

    def fft(self):
        pass

    def cria_referencia(self):
        angle = (2 * np.pi * self.frequencia)*self.sinal.time
        self.ref = np.sin(angle)

