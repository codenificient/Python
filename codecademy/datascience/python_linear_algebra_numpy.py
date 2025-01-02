import numpy as np

# Given vectors
vector_1 = np.array([-2,-6,2,3])
vector_2 = np.array([4,1,-3,8])
vector_3 = np.array([5,-7,9,0])

matrix = np.column_stack((vector_1, vector_2, vector_3))

print(matrix.shape)

print(matrix[:,2])



# Addition
A = np.array([[1,2],[3,4]])
B = np.array([[-4,-3],[-2,-1]])
A + B

# Multiplication
4 * A

# Dot product operation
v = np.array([-1,-2,-3])
u = np.array([2,2,2])
np.dot(v,u)


A = np.array([[1,2],[3,4]])
B = np.array([[-4,-3],[-2,-1]])

# one way to matrix multiply
np.matmul(A,B)
# another way to matrix multiply
A@B

