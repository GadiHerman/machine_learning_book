import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.0, 0.004, 0.00001)
s1 = 5 + 5*np.sin(2 * np.pi * 500* t)
s2 = 5*np.sin(2 * np.pi * 1000* t)
plt.plot(t, s1)
plt.plot(t, s2)
plt.grid()
plt.title("Sine wave")
plt.xlabel("time (s)")
plt.ylabel("voltage (V)")
plt.show()
