import numpy as np
import matplotlib.pyplot as plt


class Sinal():
    def __init__(self, taxa_amostragem, frequencia_rede):
        self.taxa_amostragem = taxa_amostragem
        self.time = np.arange(0, 10*(1/frequencia_rede), (1/frequencia_rede)/self.taxa_amostragem)
        self.sinal = np.zeros((len(self.time), 1)).flatten()

    def criar_sinal(self, amplitudes, defasagens, frequencias):
        for amplitude, defasagem, frequencia in zip(amplitudes, defasagens, frequencias):
            sinal = amplitude*np.sin((2*np.pi*frequencia*self.time) + defasagem)
            self.sinal = self.sinal+sinal

    def sinal_plot(self):
        if not self.sinal.max() == 0:
            figura = plt.figure()
            plt.plot(self.sinal)
            plt.show()
            return figura
        else:
            return "O sinal ainda não existe"
