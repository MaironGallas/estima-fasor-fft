import numpy as np


class SinalTeste():
    def __init__(self, amostragem, frequencia):
        self.amostragem = amostragem
        self.frequencia = frequencia

    def criar_sinal(self):
        self.time = np.arange(0, 2 * 1 / self.frequencia, (1 / self.frequencia) / self.amostragem)
        self.sinal = 10 * np.sin(2 * np.pi * 60 * self.time)