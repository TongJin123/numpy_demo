import numpy as np


a = np.array([1,1,1])
b = np.array([2,2,2])
c = np.vstack((a,b))  # 上下合并两个矩阵
d = np.hstack((a,b))  # 左右合并两个矩阵
print(c)
print(d)
print(c.shape,d.shape)  # 如果只有一维度，只返回(6,)
print(a[np.newaxis,:])  # 在列上面增加一个维度
print(b[:,np.newaxis])  # 在行上面增加一个维度
a = np.array([1,1,1])[:,np.newaxis]
b = np.array([2,2,2])[:,np.newaxis]
d = np.hstack((a,b))
print(d)
e =np.concatenate((a,b,b,a),axis=0)  # 可以将两个矩阵合并，并选择维度
print(c)