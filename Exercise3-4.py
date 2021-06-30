import numpy as np
import matplotlib.pyplot as plt
import thinkdsp
from thinkdsp import decorate
PI2 = 2 * np.pi

wave = thinkdsp.read_wave('72475__rockwehrmann__glissup02.wav')
wave.make_spectrogram(512).plot(high=5000)
decorate(xlabel='Time (s)', ylabel='Frequency (Hz)')
plt.show()