import numpy as np
"""numpy关于copy有三种情况，完全不复制、视图（view）
或者叫浅复制（shadow copy）和深复制（deep copy）"""

a = np.arange(4)

b = a
c = a
d = b
a[0] = 11  # 默认是整数
print(b)
print(c)
print(d)
d[1:3] = [22,33]
print(a)  # numpy中赋值的时候相当于python中的深拷贝
b = a.copy()  # numpy中的拷贝相当于python中的浅拷贝，拷贝之后互不影响
a[3] = 44
print(a)
print(b)
