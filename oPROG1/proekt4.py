class Vector:
    def __init__(self, *coord):
        if len(coord) == 0:
            self.x = self.y = self.z = 0
        elif len(coord) == 1:
            if isinstance(coord[0], int):
                self.x = self.y = self.z = coord[0]
            else:
                self.x, self.y, self.z = coord[0]
        elif len(coord) == 3:
            self.x, self.y, self.z = coord




   

    def length(self):
        return(self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __abs__(self):
        return self.length()

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def __mul__(self, num):
        return Vector(self.x * num, self.y * num, self.z * num)



    def scalar_product(self, other):
        return int(self.x * other.x + self.y * other.y + self.z * other.z)

    def __xor__(self, other):
        return Vector(self.y * other.z - self.z * other.y, self.z * other.x)

    @staticmethod
    def triple_product(a, b, c):
        return a*(b^c)

    def __or__(self, other):
        if (self * other == 0):
            return True
        else:
            return False

    @staticmethod
    def are_complanar(a, b, c):
        if a.triple_product(a, b, c) == 0:
            return True
        else:
            return False


a = Vector([1,2,3])
b = Vector(4,5,6)
c = a + b
print(a, b, c)
a += c
print(a)
print(b.length())
print(abs(a))
a -= b
print(a)
c = c * 2
print(c)
b = -b
print(b)
print(a.scalar_product(c))
print(a^c)
print(a.triple_product(b,c))
print(b|c)
print(a.are_complanar(b, c))

