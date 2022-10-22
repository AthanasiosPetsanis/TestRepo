import math
import numpy as np
import matplotlib.pyplot as plt

lul = np.arange(0,10,0.01)
cos_lul = np.cos(lul*math.pi)
print('lul')
plt.plot(cos_lul)
plt.show()