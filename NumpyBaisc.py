import numpy as np
#版本字符串存储在version中
print(np.__version__)

#numpy用于处理数组。
#numpy中的数组对象称为《ndarray》
#使用array()函数创建《ndarray》对象
arr = np.array([1,2,3,4])
arr1 = np.array((1,2,3,4,5))
print(arr,type(arr))
print(arr1,type(arr1))

#数组中的维：数组深度的一个级别。
#数组深度即嵌套数组指的是将数组作为元素的数组

## 0-D 数组/Scalars，数组中的每个值都是一个0-D数组
a = np.array(60)
print(arr,type(a))
## 1-D数组：元素为0-D数组的数组
b = np.array([1,2,3,4,5,6])
print(b)
## 2-D数组： 元素为1-D数组的数组
##通常用于表示矩阵和二阶张量。numpy用于专门矩阵运算的子模块：<numpy.mat>
c = np.array([[1,2,3,4,5],[4,5,4,5,5],[1,2,3,4,5]])
print(c)
##3-D数组
d = np.array([[[1,2,3],[1,2,3],[4,5,6]]])
print(d)

###用<ndim>属性检查数组维数
print(a.ndim,b.ndim,c.ndim,d.ndim)

arr = np.array([1,2,3,4],ndmin = 5)
print(arr,arr.ndim)


