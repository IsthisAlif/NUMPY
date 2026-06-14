import numpy as np

array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                  [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '_']]])

#print(array.ndim)
#print(array.shape)
#print(array[0, 1, 1])

word = array[2, 0, 0] + array[2, 0, 2] + array[1, 2, 0]

print(word)