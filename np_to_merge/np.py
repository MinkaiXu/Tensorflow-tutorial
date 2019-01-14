import numpy as np

a = np.array([[2, 5, 6],
              [9, 5, 7]])  # no dot in array
print(a.ndim, '\n',
      a.shape, '\n',
      a.size)
print('---------------------------------------')


a = np.array([[2, 255, 59],
              [58, 89, 6]], dtype=np.int)
# int int64 int32 int16 int8
# float float128 float64 float32 float16
# bool
# complex 64 128 256
print(a.dtype)
a = np.zeros((3, 4), dtype=np.int)
print(a)
a = 2*np.ones((3, 4), dtype=np.int)
print(a)
a = np.empty((3, 4), dtype=np.int)
print(a)
a = np.arange(10, 22).reshape((3, 4))
print(a)  # 返回true和false的矩阵
a = np.linspace(1, 10, 6).reshape((2, 3))
# (a,b,c)->(b-a)/(c-1)
# linspace contain the boundary value
print(a)
print('---------------------------------------')

a = np.arange(4, 8).reshape((2, 2))
print(a*a)  # multiple each one
print(np.dot(a, a))  # multiple the matrix
print(a.dot(a))  # multiple the matrix
print(5*np.sin(a))
print(a == 7)
a = np.random.random((3, 3))
print(a)
print(np.max(a), '\n',
      np.sum(a, axis=1), '\n',  # axis=1,hang;axis=0,lie
      np.min(a),
      a.mean())  # =np.mean(a)
print('---------------------------------------')

A = np.arange(14, 5, -1).reshape((3, 3))
print(np.argmin(A))  # print the index of min 是‘一个’数
print(np.argmax(A))  # print the index of max 是‘一个’数
print(np.median(A))
print(np.cumsum(A))  # 累加
print(np.diff(A))  # 差分
print(A)
print(np.sort(A))  # sort 会使原矩阵改变
print(A.T)  # =np.transpose(A)
print((A.T).dot(A))
print(np.clip(A, 5, 9))
print(np.mean(A, axis=1))
# axis = 0
# axis = 1
print('---------------------------------------')

# the index of array
A = np.arange(3, 15).reshape(3, 4)
print(A)
print(A[2, 1])  # A[2,1]=A[2][1]
print(A[:, 1])
for row in A:
    print(row)  # print each row in A 行
for clm in A.T:
    print(clm)  # print each column through the transform of A 列
print(A.flatten()) # 转化为一维的list
print(A.flatten().shape)
for a in A.flat:
    print(a)
print('---------------------------------------')

# the merge of array
a = np.array([1, 1, 1])  # note!!: not a matrix
b = np.array([2, 2, 2])
c = np.vstack((a, b))  # vertical stack
d = np.hstack((a, b))  # horizontal stack
print(c, '\n', d)
print(a.shape, c.shape, d.shape)
print(a[:, np.newaxis])  # add a dimension in column
print(b.reshape(3, 1))  # from a sequence to a matrix
# above two are the same
a = a[:, np.newaxis]
b = b[:, np.newaxis]
print(np.concatenate((a, b, b, a), axis=1))
# note for the bounds for dimension of array
print('---------------------------------------')

# the segmentation of array
