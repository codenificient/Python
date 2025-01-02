import numpy as np

# Given
A = np.array([[1,-1,1], [0,1,0], [-1,2,1]])
B = np.array([[0.5,1.5,-0.5], [0,1,0], [0.5,-0.5,0.5]])

AB = np.matmul(A,B)
BA = np.matmul(B,A)
print(AB, "\n")

print(BA)

print("\n", A.T)

print("\n", B.T)


# Magnitude of a vector
v = np.array([2,-4,1])
v_norm = np.linalg.norm(v)

# Matrix inverse
A = np.array([[1,2],[3,4]])
print(np.linalg.inv(A))

# SOLVE LINEAR EQUATIONS
# each array in A is an equation from the above system of equations
A = np.array([[1,4,-1],[-1,-3,2],[2,-1,-2]])
# the solution to each equation
b = np.array([-1,2,-2])
# solve for x, y, and z
x,y,z = np.linalg.solve(A,b)
