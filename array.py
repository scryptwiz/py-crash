from array import array

# Create an array of signed integers
a = array('i', [1, 1, 2, 3, 4, 5])
print(a.count(1))
a.append(1)
print(a.count(1))
print(a)
