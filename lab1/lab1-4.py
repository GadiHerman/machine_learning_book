import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.0, 2.0, 0.01)
s = 3*np.sin(2 * np.pi * t)
plt.plot(t, s)
plt.axis([0, 2, -3.5, +3.5])
plt.grid()
plt.title("Sine wave")
plt.xlabel("time (s)")
plt.ylabel("voltage (V)")
plt.show()
