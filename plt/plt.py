# 学习到2-4, 2-4没怎么看

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y1 = 2*x + 1
y2 = 5*x**2 - 1

plt.figure()
plt.plot(x, y1)
plt.plot(x, y2, 'r--')

plt.xlim((-1, 1))
plt.ylim((-1, 3))

plt.xlabel('X')
plt.ylabel('Y')

xticks = ['bad', 'normal', 'good', 'pretty good']
plt.xticks([-1, -0.5, 0, 1], xticks)

plt.show()
