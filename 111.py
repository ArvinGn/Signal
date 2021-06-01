import thinkdsp
import thinkplot
from matplotlib import pyplot
import matplotlib


wave = thinkdsp.read_wave('170255__dublie__trumpet.wav')
segment = wave.segment(start=1.1, duration=0.3)
spectrum = segment.make_spectrum()
spectrum.band_stop(low_cutoff=700, high_cutoff=500, factor=0.01)
wave = spectrum.make_wave()
wave.write('temp2.wav')
matplotlib.pyplot.xlim(0, 2500)
spectrum.plot()
pyplot.show()
