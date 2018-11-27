import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
iris =datasets.load_iris()
print(iris)
x=iris.data[:,1]
y=iris.data[:,2]
species=iris.target
x_reduced=PCA(n_components=3).fit_transform(iris.data)#数据降维
print(x_reduced)
fig=plt.figure()
ax=Axes3D(fig)
ax.set_title('Iris Databset by PCA',size=14)
ax.scatter(x_reduced[:,0],x_reduced[:,1],x_reduced[:,2],c=species)
ax.set_xlabel('First eigenvector')
ax.set_ylabel('Second eigenvector')
ax.set_zlabel('Thrid eigenvector')
ax.w_xaxis.set_ticklabels(())
ax.w_yaxis.set_ticklabels(())
ax.w_zaxis.set_ticklabels(())
plt.show()
