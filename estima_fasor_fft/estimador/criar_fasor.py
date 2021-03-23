import numpy as np


class Fourier():
    def __init__(self, sinal):
        self.frequencia = 60
        self.amostragem = 128
        self.sinal = sinal
        self.janela_de_amostras = np.arange(0, self.amostragem, 1)

        self.cria_referencia()
        self.cria_coef_sin_cos()

    def cria_referencia(self):
        angle = (2 * np.pi * self.frequencia)*self.sinal.time
        self.ref = np.sin(angle)

    def cria_coef_sin_cos(self):
        angle = (2 * np.pi / self.amostragem) * self.janela_de_amostras
        self.cfc = np.cos(angle)
        self.cfs = - np.sin(angle)


class Fasor():
    def __init__(self, fft):
        self.fft = fft
        self.modulo = np.zeros((len(self.fft.sinal.dados) - self.fft.amostragem, 1))

    def estima_modulo(self):

        CONSTATANTE = (2/self.fft.amostragem)

        for i in range(self.fft.amostragem, len(self.fft.sinal.dados), 1):
            fftR = (np.sum(self.fft.sinal.dados[i - self.fft.amostragem:i] * self.fft.cfc))*(CONSTATANTE)
            fftI = (np.sum(self.fft.sinal.dados[i - self.fft.amostragem:i] * self.fft.cfs))*(CONSTATANTE)

            self.modulo[i - self.fft.amostragem] = np.sqrt(fftR * fftR + (fftI * fftI))

    def estima_angulo(self):
        pass

