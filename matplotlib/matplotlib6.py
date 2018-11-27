import matplotlib.pyplot as plt
import numpy as np
index=np.arange(5)
std1=[0.8,1,0.4,0.9,1.3]
values=[5,7,3,4,6]
plt.barh(index,values,xerr=std1,error_kw={'ecolor':'0.1','capsize':6},alpha=0.3,label='First')
plt.title('A Horizontal Bar Chart')
plt.yticks(index+0.4,['A','B','C','D','E'])
plt.legend(loc=5)
plt.show()