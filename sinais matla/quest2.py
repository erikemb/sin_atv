import numpy as np
import matplotlib.pyplot as plt

f = 10
overSampRate = 30
fs = overSampRate * f
noyl = 5
t = np.arange(0, noyl + 1 / f, 1 / fs)
x = np.sin(2 * np.pi * f * t)

plt.figure()
plt.plot(t, x)
plt.title(f'Seno f={f} Hz')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.show()