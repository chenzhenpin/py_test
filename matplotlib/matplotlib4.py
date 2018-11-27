import matplotlib.pyplot as plt
import numpy as np
pop=np.random.randint(0,100,100)
n,bins,patches=plt.hist(pop,bins=20)
print(n)
print(bins)
print(patches)
plt.show()