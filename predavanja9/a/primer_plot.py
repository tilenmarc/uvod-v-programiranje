import matplotlib.pyplot as plt

# import numpy as np
import math

# Data for plotting
x = [i * 2.0 * math.pi / 100 for i in range(100)]
y = [math.sin(i) for i in x]


fig, ax = plt.subplots()
ax.plot(x, y)

ax.set(
    xlabel="time (s)", ylabel="voltage (mV)", title="About as simple as it gets, folks"
)
ax.grid()

fig.savefig("test.png")
plt.show()
