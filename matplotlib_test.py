import matplotlib.pyplot as plt
import numpy as np

k = 400000
th = 3

n = 10000
u = np.random.uniform(0, 1, n)
X = (1 - u) ** (-1/th) * k

plt.xlim(400, 2000)
plt.hist(X/1000, 200, density = True, facecolor = "navy", edgecolor = "black")
plt.xlabel("Årsinntekt (i 1000 kroner)")
plt.savefig("history.png")
plt.show()