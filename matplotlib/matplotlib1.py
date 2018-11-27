import matplotlib.pyplot as plt
import numpy as np
plt.axis([0,5,0,20])
plt.title('my first plot')
plt.xlabel('counting')
plt.ylabel('square values')
plt.text(2,11,r'$y=x^2$',fontsize=20,bbox={'facecolor':'blue','alpha':0.8})
plt.plot([1,2,3,4],[1,4,9,16],'bo')
plt.plot([1,2,3,4],[0.5,2.5,4,12],'g*')
plt.grid(True)
plt.legend(['first series','second'],loc=2)
plt.show()
plt.savefig('matplotlib.png')