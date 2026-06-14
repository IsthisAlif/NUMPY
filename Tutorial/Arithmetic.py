import numpy as np

# Scalar arithmetic (single value)
array1 = np.array([1, 2, 3])

print("Scalar Arithmetic: ")
print(array1 + 1)
print(array1 - 2)
print(array1 * 3)
print(array1 / 4)
print(array1 ** 5)
print()

# Vectorized math funcs
array2 = np.array([1.01, 2.5, 3.99])

print("Vectorized math funcs: ")
print(np.sqrt(array2))
print(np.round(array2))
print(np.floor(array2))
print(np.ceil(array2))
print(np.pi)
print()

# Elemet-wise arithmetic
array3 = np.array([1, 2, 3])
array4 = np.array([4, 5, 6])

print("Elemet-wise arithmetic: ")
print(array3 + array4)
print(array3 - array4)
print(array3 * array4)
print(array3 / array4)
print(array3 ** array4)
print()

# Comparison operators
scores = np.array([91, 55, 100, 73, 82, 64])

print("Comparison operators: ")
print(scores == 100)
print(scores >= 60)
print(scores <= 60)
scores[scores < 60] = 0
print(scores)