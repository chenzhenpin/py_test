import matplotlib.pyplot as plt
import numpy as np
index=np.arange(5)
values1=[5,7,3,4,6]
values2=[6,6,4,5,7]
values3=[5,6,5,4,6]
plt.axis([0,8,0,5])
bw=0.3
plt.barh(index,values1,bw,color='b')
plt.barh(index+bw,values2,bw,color='g')
plt.barh(index+2*bw,values3,bw,color='r')
plt.title('A Bar Chart')
plt.yticks(index-0.4,['A','B','C','D','E'])
plt.show()