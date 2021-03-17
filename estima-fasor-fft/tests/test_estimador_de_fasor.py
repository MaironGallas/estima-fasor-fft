import numpy as np


class TransfomadaFourie():
    def __init__(self, amostragem, frequencia):
        self.frequencia = frequencia
        self.amostragem = amostragem
        self.janela_de_amostras = np.arange(0, self.amostragem, 1)
        self.cria_coef_sin_cos()

    def cria_coef_sin_cos(self):
        angle = (2*np.pi/self.amostragem)*self.janela_de_amostras
        self.cfc = np.cos(angle)
        self.cfs = - np.sin(angle)

    def estima_modulo(self, sinal):
        modulo = np.zeros((len(sinal)-self.amostragem, 1))

        for i in range(self.amostragem, len(sinal), 1):
            fftR = (np.sum(sinal[i-self.amostragem:i]*self.cfc))/(2/self.amostragem)
            fftI = (np.sum(sinal[i-self.amostragem:i] * self.cfs))/(2/self.amostragem)
            modulo[i-self.amostragem] = np.sqrt(fftR * fftR + (fftI * fftI))

        return modulo


def criar_sinal_teste():
    amostragem = 128
    frequencia = 60
    t = np.arange(0, 2*1/frequencia, (1/frequencia)/amostragem)
    sinal = 10*np.sin(2 * np.pi * 60 * t)
    return sinal

def test_estimar_modulo():
    sinal = criar_sinal_teste()

    fasor = TransfomadaFourie(128, 60)
    modulo = np.full((128, 0), 1)
    print(modulo)
    assert np.array_equiv(modulo, fasor.estima_modulo(sinal))
    print('Acabou')
    print(fasor.estima_modulo(sinal))
