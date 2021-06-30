from thinkdsp import SinSignal
from matplotlib import pyplot

signal = (SinSignal(freq=400, amp=1.0) +
          SinSignal(freq=600, amp=0.5) +
          SinSignal(freq=800, amp=0.25))
signal.plot()
pyplot.show()

wave2 = signal.make_wave(duration=1)
wave2.write('t0.wav')


spectrum = wave2.make_spectrum()
spectrum.plot(high=2000)
pyplot.show()

signal += SinSignal(freq=450)
wave3 = signal.make_wave()
wave3.write('t1.wav')