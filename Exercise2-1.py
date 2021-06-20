from thinkdsp import Sinusoid
from thinkdsp import normalize, unbias
import numpy as np
import matplotlib.pyplot as plt
from thinkdsp import decorate
from thinkdsp import SquareSignal
from thinkdsp import TriangleSignal


class SawtoothSignal(Sinusoid):

    def evaluate(self, ts):
        cycles = self.freq * ts + self.offset / np.pi / 2
        frac, _ = np.modf(cycles)
        ys = normalize(unbias(frac), self.amp)
        return ys



sawtooth = SawtoothSignal().make_wave(duration=0.5, framerate=40000)
sawtooth.write('Wav2-1-1.wav')
# 锯齿波频谱
sawtooth.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')
plt.show()

# 方波频谱
sawtooth.make_spectrum().plot(color='gray')
square = SquareSignal(amp=0.5).make_wave(duration=0.5, framerate=40000)
square.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')
plt.show()

# 与三角波相比，锯齿波的衰减速度没那么快。减少方波的振幅，使它们具有可比性。
sawtooth.make_spectrum().plot(color='gray')
triangle = TriangleSignal(amp=0.79).make_wave(duration=0.5, framerate=40000)
triangle.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')
plt.show()