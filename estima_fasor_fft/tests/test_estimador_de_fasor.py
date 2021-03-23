import pytest
from estima_fasor_fft.estimador.criar_fasor import Fasor
from estima_fasor_fft.estimador.criar_sinal import SinalTeste

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
    [60, 128]
)
def test_criar_sinal(frequencia):
    sinal = SinalTeste(128, frequencia)
    sinal.criar_sinal()

def test_modulo_fasor():
    sinal = SinalTeste(128, 60)
    sinal.criar_sinal()
    fasor = Fasor(sinal)
    fasor.fft()

