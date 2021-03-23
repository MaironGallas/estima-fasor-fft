import numpy as np
import pytest
from estima_fasor_fft.estimador.criar_fasor import Fasor, Fourier
from estima_fasor_fft.estimador.criar_sinal import SinalTeste
import matplotlib.pyplot as plt


class TransfomadaFourie():
    def __init__(self, amostragem, frequencia):
        self.frequencia = frequencia
        self.amostragem = amostragem
        self.janela_de_amostras = np.arange(0, self.amostragem, 1)
        self.cria_coef_sin_cos()

    def cria_coef_sin_cos(self):
        angle = (2 * np.pi / self.amostragem) * self.janela_de_amostras
        self.cfc = np.cos(angle)
        self.cfs = - np.sin(angle)

    def estima_modulo(self, sinal):
        modulo = np.zeros((len(sinal) - self.amostragem, 1))

        for i in range(self.amostragem, len(sinal), 1):
            fftR = (np.sum(sinal[i - self.amostragem:i] * self.cfc)) / (2 / self.amostragem)
            fftI = (np.sum(sinal[i - self.amostragem:i] * self.cfs)) / (2 / self.amostragem)
            modulo[i - self.amostragem] = np.sqrt(fftR * fftR + (fftI * fftI))

        return modulo


@pytest.mark.parametrize(
    'frequencia',
    [60, 180]
)
def test_criar_sinal(frequencia):
    amplitude = 10
    amostragem = 128

    sinal = SinalTeste(amplitude, amostragem, frequencia)
    sinal.criar_sinal()
    assert sinal.amostragem == 128


def test_modulo_fasor():
    amplitude = 10
    amostragem = 128
    frequencia = 60
    defasagem = 0

    sinal = SinalTeste(amplitude, defasagem, amostragem, frequencia)
    sinal.criar_sinal()

    fft_cfg = Fourier(sinal)  # Configurações do Fourier
    fasor = Fasor(fft_cfg)
    fasor.estimar()

    assert (fasor.modulo[0] == amplitude)


def test_angulo_fasor():
    amplitude = 10
    amostragem = 128
    frequencia = 60
    defasagem = np.pi/2

    sinal = SinalTeste(amplitude, defasagem, amostragem, frequencia)
    sinal.criar_sinal()

    fft_cfg = Fourier(sinal)  # Configurações do Fourier
    fasor = Fasor(fft_cfg)
    fasor.estimar()
    assert (fasor.fase[0] < 90.1 and fasor.fase[0] > 89.8)
