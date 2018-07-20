import numpy as np

a = np.arange(12).reshape((3,4))  # 生成一个3行4列的矩阵
print(a)
print(np.split(a,2,axis=1))  # 对列进行纵向分割，分成2块
print(np.split(a,3,axis=0))  # 对行进行横向分割，分成3块
print(np.array_split(a,3,axis=1))  # 对列进行不等量分割
print(np.vsplit(a,3))  # 纵向分割
print(np.hsplit(a,2))  # 横向分割