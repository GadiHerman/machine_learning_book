import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0.0, 3.0, 0.1)
print(t)
plt.plot(t, t, 'r--')
plt.plot(t, t**2, 'g^')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
