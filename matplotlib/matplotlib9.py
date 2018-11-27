import matplotlib.pyplot as plt
import numpy as np
series1=np.array([3,4,5,3])
series2=np.array([1,2,2,5])
series3=np.array([2,3,3,4])
index=np.arange(4)
plt.axis([0,4,0,15])
plt.bar(index,series1,color='r')
plt.bar(index,series2,color='b',bottom=series1)
plt.bar(index,series3,color='g',bottom=(series1+series2))
plt.xticks(index-0.4,['jan15','feb15','mar15','apr15'])
plt.show()