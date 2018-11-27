import matplotlib.pyplot as plt
import numpy as np
index=np.arange(5)
std1=[0.8,1,0.8,0.9,1.3]
values=[5,7,3,4,6]
plt.bar(index,values,yerr=std1,error_kw={'ecolor':'0.1','capsize':6},alpha=0.3,label='First')
plt.title('A Bar Chart')
plt.xticks(index,['A','B','C','D','E'])
plt.legend(loc=2)
plt.show()