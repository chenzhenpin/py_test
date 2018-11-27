import numpy as np 
import pandas as pd 
frame1=pd.DataFrame({'id':['ball','pencil','pen','mug','ashtray'],'price':[12.33,11.44,33.21,13.21,33.63]})
print(frame1)
frame2=pd.DataFrame({'id':['pencil','pencil','ball','pen'],'color':['white','red','red','black']})
print(frame2)
print(pd.merge(frame1,frame2))