import numpy as np

# Explicit COLUMN vector: shape (3, 1)
u = np.array ([[5],
                [3],
                [-4]])

v = np.array ([[-1],
              [5],
              [2]],)
w = np.array ([[3],
              [-1],
              [-2]],)
print(5*u - 2*v)
print()
print(-2*u + 4*v - 3*w)
#row vector: shape (1, 3)
a = np.array ([2, -5, 6])
b = np.array ([8, 2, -3])
print(np.dot(a,b))
print()
c = np.array ([4, 2, -3, 5, -1])
d = np.array ([2, 6, -1, -4, 8])
print(np.dot(c,d))
print()