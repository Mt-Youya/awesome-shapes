import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 1000)

x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

plt.figure(figsize=(8, 8), facecolor="black")
plt.plot(x, y, color="red", linewidth=2)
plt.title("Love You", fontsize=20, color="white")
plt.gca().set_facecolor("black")
plt.axis("equal")
plt.grid(False)
plt.xticks([])
plt.yticks([])

plt.show()
