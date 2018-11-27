import numpy as np
from sklearn import datasets

iris=datasets.load_iris()
x=iris.data
y=iris.target
print(iris.data)
print(y)
i=np.random.permutation(len(iris.data))
x_train=x[i[:-10]]
y_train=y[i[:-10]]
x_test=x[i[-10:]]
y_test=y[i[-10:]]
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier()
knn.fit(x_train,y_train)#训练模型
print(knn.predict(x_test))#预测结果
print(y_test)