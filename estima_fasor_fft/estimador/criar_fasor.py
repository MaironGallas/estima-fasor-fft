import math

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
        self.fase = np.zeros((len(self.fft.sinal.dados) - self.fft.amostragem, 1))

    def estimar(self):

        CONSTANTE = (2/self.fft.amostragem)

        for i in range(self.fft.amostragem, len(self.fft.sinal.dados), 1):
            fftr = (np.sum(self.fft.sinal.dados[i - self.fft.amostragem:i] * self.fft.cfc))*CONSTANTE
            ffti = (np.sum(self.fft.sinal.dados[i - self.fft.amostragem:i] * self.fft.cfs))*CONSTANTE

            fftr_ref = (np.sum(self.fft.ref[i - self.fft.amostragem:i] * self.fft.cfc))*CONSTANTE
            ffti_ref = (np.sum(self.fft.ref[i - self.fft.amostragem:i] * self.fft.cfs))*CONSTANTE

            ffta = math.atan2(ffti, fftr) * 57.295779
            ffta_ref = math.atan2(ffti_ref, fftr_ref) * 57.295779

            self.modulo[i - self.fft.amostragem] = np.sqrt(fftr * fftr + (ffti * ffti))
            self.fase[i - self.fft.amostragem] = self.calcular_angulo(ffta, ffta_ref)

    def calcular_angulo(self, ffta, ref_angulo):
        x = ffta - 90
        if x <= -180:
            x = x + 360

        xRef = ref_angulo - 90
        if xRef <= -180:
            xRef = xRef + 360

        while xRef <= -180:
            xRef = xRef + 360

        angulo = x - xRef

        if angulo >= 180:
            angulo = angulo - 360
        if angulo <= -180:
            angulo = angulo + 360
        if (angulo >= -0.0001) and (angulo <= 0.0001):
            angulo = 0

        return angulo
