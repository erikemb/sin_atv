import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

for i in range(1, 6):
    N = i  # Ordem da série
    Fs = 8192  # Freq de amostragem
    t = np.linspace(0, 1 - 1 / 8192, Fs)
    f = 2
    amp = 1
    
    ax = fig.add_subplot(3, 2, N)
    h, = ax.plot(np.nan, np.nan)
    tt = f"Ordem {N}"
    ax.set_title(tt)
    ax.axis([0, 1, -0.2, 1.2])
    
    res = amp / 2
    
    for k in range(1, N + 1):
        res = res - (amp / (k * np.pi)) * np.sin(2 * np.pi * k * f * t)
        h.set_data(t, res)
        # plt.pause(0.1)

N = 500  # Ordem da série
Fs = 8192  # Freq de amostragem
t = np.linspace(0, 1 - 1 / 8192, Fs)
f = 2
amp = 1

ax = fig.add_subplot(3, 2, 6)
h, = ax.plot(np.nan, np.nan)
tt = f"Ordem {N}"
ax.set_title(tt)
ax.axis([0, 1, -0.2, 1.2])

res = amp / 2

for k in range(1, N + 1):
    res = res - (amp / (k * np.pi)) * np.sin(2 * np.pi * k * f * t)
    h.set_data(t, res)
    # plt.pause(0.1)

plt.show()