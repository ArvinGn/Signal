import thinkdsp
from matplotlib import pyplot

wave3 = thinkdsp.read_wave('170255__dublie__trumpet.wav')

def stretch(wave, factor):
    wave.ts *= factor
    wave.framerate /= factor


stretch(wave3, 0.5)
wave3.write('tt1.wav')

wave3.plot()
pyplot.show()