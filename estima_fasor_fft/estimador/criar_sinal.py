import numpy as np


class SinalTeste():
    def __init__(self, amplitude, defasagem, amostragem, frequencia):
        self.defasagem = defasagem
        self.amplitude = amplitude
        self.amostragem = amostragem
        self.frequencia = frequencia

    def criar_sinal(self):
        self.time = np.arange(0, 2 * 1 / self.frequencia, (1 / self.frequencia) / self.amostragem)
        self.dados = self.amplitude * np.sin((2 * np.pi * self.frequencia * self.time) + self.defasagem)

    def criar_sinal_duas_frequencias(self):
        self.time = np.arange(0, 2 * 1 / self.frequencia, (1 / self.frequencia) / self.amostragem)
        self.dados = self.amplitude * np.sin((2 * np.pi * self.frequencia * self.time) + self.defasagem) + (
            (self.amplitude / 2) * np.sin((2 * np.pi * self.frequencia * 3 * self.time))
        )
