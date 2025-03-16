point = {'x': 1, 'y': 2, 'z': 3}
point = dict(x=1, y=2, z=3)
point['x'] = 10
print(point['x'])
print(point.get('a', 10))
del point['x']
print(point)

# Looping through dictionary
for key, value in point.items():
    print(key, value)

# Dictionary comprehension
values = {x: x * 2 for x in range(5)}
print(values)
