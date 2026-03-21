import numpy as np 

X = np.array([[1,2,3] , [4,5,6]])
u = np.mean(X,axis=0)
dev = np.std(X , axis = 0) 
print((X-u)/dev)

