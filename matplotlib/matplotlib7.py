import matplotlib.pyplot as plt
import numpy as np
index=np.arange(5)
values1=[5,7,3,4,6]
values2=[6,6,4,5,7]
values3=[5,6,5,4,6]
bw=0.3
plt.bar(index,values1,bw,color='b')
plt.bar(index+bw,values2,bw,color='g')
plt.bar(index+2*bw,values3,bw,color='r')
plt.title('A Bar Chart')
plt.xticks(index,['A','B','C','D','E'])
plt.show()