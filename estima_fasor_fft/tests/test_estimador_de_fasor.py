import numpy as np
import pytest
from estima_fasor_fft.estimador.criar_fasor import Fasor, Fourier
from estima_fasor_fft.estimador.criar_sinal import SinalTeste


@pytest.mark.parametrize(
    'frequencia',
    [60, 180]
)
def test_criar_sinal(frequencia):
    amplitude = 10
    amostragem = 128
    defasagem = 0

    sinal = SinalTeste(amplitude, defasagem, amostragem, frequencia)
    sinal.criar_sinal()

    assert sinal.amostragem == 128


def test_criar_sinal_duas_frequencias():
    amplitude = 10
    amostragem = 128
    defasagem = 0
    frequencia = 60

    sinal = SinalTeste(amplitude, defasagem, amostragem, frequencia)
    sinal.criar_sinal_duas_frequencias()

    assert sinal.amostragem == amostragem


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


@pytest.mark.parametrize(
    'frequencia , amplitude',
    [(60, 5), (180, 10)]
)
def test_fasores(frequencia, amplitude):
    amostragem = 128
    defasagem = 0

    sinal = SinalTeste(amplitude, defasagem, amostragem, frequencia)
    sinal.criar_sinal_duas_frequencias()

    fft_cfg = Fourier(sinal)  # Configurações do Fourier
    fasor = Fasor(fft_cfg)
    fasor.estimar()
