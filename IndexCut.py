import numpy as np

#访问数组元素
a = np.array([1,2,3,4,5])
print(a[0])
print(a[1]+a[3])
#访问2-D数组
b = np.array([[1,2,3,4],[5,6,7,8]])
print("3rd of 2dim : ", b[1,2])
print("4rd of 1dim : ", b[0,3])
#访问3-D数组
c = np.array([[[1,2,3],[4,5,6]],[[1,7,9],[11,24,76]]])
print(c[0,1,2])
print(c[1,0,1])
#负索引
print("Last element from 2nd dim : ",b[1,-1])

#裁切数组：将元素从一个给定的索引带到另一个给定的索引
#[start:end:step]
# start默认值为0
# end默认值为该维度内数组的长度
# step默认值为1
# 结果包括开始索引，不包括结束索引
a = np.array([1,2,3,4,5,6,7,8])
print(a[0:7])
print(a[3:6])
print(a[0:])
print(a[:4])
print(a[-3:-1])
print(a[1:5:2])
print(a[1::2])
#裁切2-D数组
b = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(b[1,0:2])
print(b[0:2,2])
print(b[0:2,0:3])