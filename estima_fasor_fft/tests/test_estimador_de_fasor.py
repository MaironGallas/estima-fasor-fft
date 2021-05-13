import pytest
from matplotlib import figure
from pytest import fixture
import numpy as np

from estima_fasor_fft.estimador.criar_fasor import Fourier, Fasor
from estima_fasor_fft.estimador.criar_sinal import Sinal


@fixture
def inputs():
    taxa_amostragem = 128
    frequencia_rede = 60
    return taxa_amostragem, frequencia_rede


@fixture
def sinal():
    amplitudes = [50, 25, 5]
    defasagens = [np.pi/2, np.pi/4, np.pi]
    frequencias = [60, 120, 180]
    taxa_amostragem = 128
    frequencia_rede = 60
    sinal = Sinal(taxa_amostragem, frequencia_rede)
    sinal.criar_sinal(amplitudes, defasagens, frequencias)
    sinal.sinal_plot()
    return sinal

@pytest.mark.parametrize('amplitudes, defasagens, frequencias', [([10], [0], [60])])
def test_criar_sinal(amplitudes, defasagens, frequencias, inputs):
    sinal = Sinal(inputs[0], inputs[1])
    sinal.criar_sinal(amplitudes, defasagens, frequencias)
    assert sinal.taxa_amostragem == 128


@pytest.mark.parametrize('amplitudes, defasagens, frequencias', [([10], [0], [60])])
def test_criar_plot_sinal(amplitudes, defasagens, frequencias, inputs):
    sinal = Sinal(inputs[0], inputs[1])
    sinal.criar_sinal(amplitudes, defasagens, frequencias)
    figura = sinal.sinal_plot()
    assert type(figura) is figure.Figure


def test_error_plot_sinal(inputs):
    sinal = Sinal(inputs[0], inputs[1])
    figura = sinal.sinal_plot()
    assert figura == "O sinal ainda não existe"

@pytest.mark.parametrize('amplitudes, defasagens, frequencias', [([10, 50], [0, 0], [60, 180])])
def test_criar_sinal_distorcido(amplitudes, defasagens, frequencias, inputs):
    sinal = Sinal(inputs[0], inputs[1])
    sinal.criar_sinal(amplitudes, defasagens, frequencias)
    assert sinal.taxa_amostragem == 128


@pytest.mark.parametrize('amplitudes, defasagens, frequencias', [([10, 1], [0, 0], [60, 180])])
def test_criar_plot_sinal_distorcido(amplitudes, defasagens, frequencias, inputs):
    sinal = Sinal(inputs[0], inputs[1])
    sinal.criar_sinal(amplitudes, defasagens, frequencias)
    figura = sinal.sinal_plot()
    assert type(figura) is figure.Figure

def test_criar_conf_fft_e_fasor(sinal):
    cfg_fft = Fourier(sinal, 60)
    assert cfg_fft.frequencia == 60
    fasor = Fasor(cfg_fft)
    assert type(fasor) == Fasor
    fasor.estimar()
    assert 50.001 > fasor.modulo[0][0] > 49.999
    assert 25.001 > fasor.modulo[1][0] > 24.999
    assert 5.001 > fasor.modulo[2][0] > 4.999
    assert (90.1 > fasor.fase[0][0] > 89.8)
