from thinkdsp import decorate
from thinkdsp import SquareSignal
from thinkdsp import SinSignal
import matplotlib.pyplot as plt

square = SquareSignal(1500).make_wave(duration=0.5, framerate=10000)
square.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')
plt.show()

square.write('Wav2-2-1.wav')
SinSignal(500).make_wave(duration=0.5, framerate=10000).write('Wav2-2-2.wav')