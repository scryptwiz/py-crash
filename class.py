class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        print(self.x, self.y)

    def set_coordinates(self, x, y):
        self.x = x,
        self.y = y,

p = Point(3, 4)
p.set_coordinates(5, 6)
p.get_coordinates()

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self._passengers = []

    def open_seats(self):
        return self.capacity - len(self._passengers)
        
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self._passengers.append(name)
        return True
flight = Flight(3)
print(flight.add_passenger("Harry"))
print(flight.add_passenger("Kelvin"))
print(flight.add_passenger("Kelvide"))

class Test:
    def __init__(self):
        pass

    def print(self):
        print("Hello World")

t = Test()
t.print()

class Points:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    @classmethod
    def zero(cls):
        return cls(0, 0)
    
point = Points.zero()
print(point.x, point.y)

point1= Points(1, 2)
point2 = Points(1, 2)
print(point1 == point2)