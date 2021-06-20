from thinkdsp import decorate
from thinkdsp import TriangleSignal
import matplotlib.pyplot as plt

def filter_spectrum(spectrum):
    # avoid division by 0
    spectrum.hs[1:] /= spectrum.fs[1:]
    spectrum.hs[0] = 0


wave = TriangleSignal(freq=440).make_wave(duration=0.5)
wave.write("Wav2-4-1.wav")

spectrum = wave.make_spectrum()
spectrum.plot(high=10000, color='gray')
filter_spectrum(spectrum)
spectrum.scale(440)
spectrum.plot(high=10000)
decorate(xlabel='Frequency (Hz)')
plt.show()

filtered = spectrum.make_wave()
filtered.write("Wav2-4-2.wav")
