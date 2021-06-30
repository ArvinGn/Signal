import numpy as np
import matplotlib.pyplot as plt

from thinkdsp import decorate

from thinkdsp import SinSignal
signal = SinSignal(freq=440)
duration = signal.period * 30.25
wave = signal.make_wave(duration)
spectrum = wave.make_spectrum()

spectrum.plot(high=880)
decorate(xlabel='Frequency (Hz)')
plt.show()

for window_func in [np.bartlett, np.blackman, np.hamming, np.hanning]:
    wave = signal.make_wave(duration)
    wave.ys *= window_func(len(wave.ys))

    spectrum = wave.make_spectrum()
    spectrum.plot(high=880, label=window_func.__name__)

decorate(xlabel='Frequency (Hz)')
plt.show()
# 四种方法都能很好地减少泄漏。巴特利特滤波器留下一些残余的“振铃”。汉明滤波器耗散的能量最少。

