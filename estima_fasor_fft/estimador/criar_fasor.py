import math
import numpy as np


class Fourier():
    def __init__(self, sinal, frequencia):
        self.cfc_lista = []
        self.cfs_lista = []
        self.frequencia = frequencia
        self.sinal = sinal
        self.janela_de_amostras = np.arange(0, self.sinal.taxa_amostragem, 1)
        self.taxa_amostragem = self.sinal.taxa_amostragem
        self.cria_referencia()
        self.cria_coef_sin_cos()

    def cria_referencia(self):
        angle = (2 * np.pi * self.frequencia)*self.sinal.time
        self.ref = np.sin(angle)

    def cria_coef_sin_cos(self):
        for harmonica in range(1, 10, 1):
            angle = (2 * np.pi * harmonica / self.sinal.taxa_amostragem) * self.janela_de_amostras #Multiplicar no pi pelo numero de harmonica
            cfc = np.cos(angle)
            cfs = - np.sin(angle)
            self.cfc_lista.append(np.copy(cfc))
            self.cfs_lista.append(np.copy(cfs))


class Fasor():
    def __init__(self, fft):
        self.fft = fft
        self.modulo = []
        self.fase = []

    def estimar(self):
        modulo = np.zeros((len(self.fft.sinal.sinal) - self.fft.taxa_amostragem, 1))
        fase = np.zeros((len(self.fft.sinal.sinal) - self.fft.taxa_amostragem, 1))

        CONSTANTE = (2/self.fft.taxa_amostragem)

        for indice_harmonica in range(0, 9, 1):
            harmonica = indice_harmonica + 1
            for i in range(self.fft.taxa_amostragem, len(self.fft.sinal.sinal), 1):
                fftr = (np.sum(self.fft.sinal.sinal[i - self.fft.taxa_amostragem:i] * self.fft.cfc_lista[indice_harmonica]))*CONSTANTE
                ffti = (np.sum(self.fft.sinal.sinal[i - self.fft.taxa_amostragem:i] * self.fft.cfs_lista[indice_harmonica]))*CONSTANTE

                fftr_ref = (np.sum(self.fft.ref[i - self.fft.taxa_amostragem:i] * self.fft.cfc_lista[indice_harmonica]))*CONSTANTE
                ffti_ref = (np.sum(self.fft.ref[i - self.fft.taxa_amostragem:i] * self.fft.cfs_lista[indice_harmonica]))*CONSTANTE

                ffta = math.atan2(ffti, fftr) * 57.295779
                ffta_ref = math.atan2(ffti_ref, fftr_ref) * 57.295779

                modulo[i - self.fft.taxa_amostragem] = np.sqrt(fftr * fftr + (ffti * ffti))
                fase[i - self.fft.taxa_amostragem] = self.calcular_angulo(ffta, ffta_ref, harmonica)

            self.modulo.append(np.copy(modulo))
            self.fase.append(np.copy(fase))

    def calcular_angulo(self, ffta, ref_angulo, harmonica):
        x = ffta - 90
        if x <= -180:
            x = x + 360

        xref = ref_angulo - 90
        if xref <= -180:
            xref = xref + 360

        xref = xref*harmonica

        while xref <= -180:
            xref = xref + 360

        while xref >= 180:
            xref = xref - 360

        angulo = x - xref

        if angulo >= 180:
            angulo = angulo - 360
        if angulo <= -180:
            angulo = angulo + 360
        if (angulo >= -0.0001) and (angulo <= 0.0001):
            angulo = 0

        return angulo
