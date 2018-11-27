import matplotlib.pyplot as plt
labels=['Nokia','Samsung','Apple','Lumia']
values=[10,30,45,15]
colors=['yellow','green','red','blue']
explode=[0.3,0.1,0,0]
plt.pie(values,labels=labels,colors=colors,explode=explode,shadow=True,autopct='%1.1f%%',startangle=180)
plt.title('A Pie Chart')
plt.axis('equal')
plt.show()
