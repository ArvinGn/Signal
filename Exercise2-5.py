
from thinkdsp import Sinusoid
from thinkdsp import normalize, unbias
import numpy as np
import matplotlib.pyplot as plt
from thinkdsp import decorate
from thinkdsp import CosSignal
from thinkdsp import ParabolicSignal

class SawtoothSignal(Sinusoid):

    def evaluate(self, ts):
        cycles = self.freq * ts + self.offset / np.pi / 2
        frac, _ = np.modf(cycles)
        ys = normalize(unbias(frac), self.amp)
        return ys

def filter_spectrum(spectrum):
    # avoid division by 0
    spectrum.hs[1:] /= spectrum.fs[1:]
    spectrum.hs[0] = 0


freq = 500
signal = SawtoothSignal(freq=freq)
wave = signal.make_wave(duration=0.5, framerate=20000)
wave.write("Wav2-5-1.wav")

spectrum = wave.make_spectrum()
spectrum.plot()
decorate(xlabel='Frequency (Hz)')
plt.show()

spectrum.plot(color='gray')
filter_spectrum(spectrum)
spectrum.scale(freq)
spectrum.plot()
decorate(xlabel='Frequency (Hz)')
plt.show()

wave = spectrum.make_wave()
wave.write("Wav2-5-2.wav")
wave.segment(duration=0.01).plot()
decorate(xlabel='Time (s)')
plt.show()


freqs = np.arange(500, 9500, 500)
amps = 1 / freqs**2
signal = sum(CosSignal(freq, amp) for freq, amp in zip(freqs, amps))
print(signal)

spectrum = wave.make_spectrum()
spectrum.plot()
decorate(xlabel='Frequency (Hz)')
plt.show()

wave = signal.make_wave(duration=0.5, framerate=20000)
wave.write("Wav2-5-3.wav")

wave.segment(duration=0.01).plot()
decorate(xlabel='Time (s)')
plt.show()


wave = ParabolicSignal(freq=500).make_wave(duration=0.5, framerate=20000)
wave.write("Wav2-5-4.wav")

wave.segment(duration=0.01).plot()
decorate(xlabel='Time (s)')
plt.show()

spectrum = wave.make_spectrum()
spectrum.plot()
decorate(xlabel='Frequency (Hz)')
plt.show()

