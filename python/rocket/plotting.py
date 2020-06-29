import numpy as np
import matplotlib.pyplot as plt
data1 = np.load("launcher1.npz")
data2 = np.load("launcher2.npz")
data3 = np.load("launcher3.npz")
# noise = np.array([ np.random.normal(0,10000) for i in range(1200)])
plt.plot((data1["costs"][0:1200] + data2["costs"][0:1200] + data3["costs"][0:1200])/3 )
plt.xlabel("Iterations")
plt.ylabel("Cost")
plt.show()
