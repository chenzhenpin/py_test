import matplotlib.pyplot as plt
import numpy as np
x=np.arange(-2*np.pi,2*np.pi,0.01)
y=np.sin(3*x)/x
y2=np.sin(2*x)/x
plt.plot(x,y,'b')
plt.plot(x,y2,'r')
plt.xticks([-2*np.pi,-np.pi,0,np.pi,2*np.pi],[r'$-2\pi$',r'$-\pi$',r'$0$',r'$+\pi$',r'$+2\pi$'])
plt.yticks([-1,0,+1,+2,+3],[r'$-1$',r'$0$',r'$+1$',r'$+2$',r'$+3$'])
plt.show()