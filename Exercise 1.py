import thinkdsp
import thinkplot
from matplotlib import pyplot
import matplotlib

# 音频
wave = thinkdsp.read_wave('170255__dublie__trumpet.wav')
wave.plot()
pyplot.show()

# 在原音频中取出1.1s-1.4s，这个为高音稳定的片段
segment = wave.segment(start=1.1, duration=0.3)
wave = segment
wave.write("output1.wav")
segment.plot()
pyplot.show()

segment.segment(start=1.1, duration=0.005).plot()
pyplot.show()

# 这是频谱的样子
spectrum = segment.make_spectrum()
spectrum.plot(high=7000)
pyplot.show()
# 放大基频和主频
spectrum = segment.make_spectrum()
spectrum.plot(high=1000)
pyplot.show()

# 使用低通滤波器，所有高于700的频率衰减99%
spectrum.low_pass(cutoff=700, factor=0.01)
wave = spectrum.make_wave()
wave.write('temp0.wav')
matplotlib.pyplot.xlim(0, 2500)
spectrum.plot()
pyplot.show()
# 使用高通滤波器，所有低于500的频率衰减99%
spectrum.high_pass(cutoff=500, factor=0.01)
wave = spectrum.make_wave()
wave.write('temp1.wav')
wave.write('temp0.wav')
matplotlib.pyplot.xlim(0, 2500)
spectrum.plot()
pyplot.show()
#
spectrum.band_stop(low_cutoff=700, high_cutoff=200, factor=0.01)
wave = spectrum.make_wave()
wave.write('temp2.wav')
wave.write('temp0.wav')
matplotlib.pyplot.xlim(0, 2500)
spectrum.plot()
pyplot.show()



