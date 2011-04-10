from math import sqrt

class Vector:
    """
    Super basit bir 2d vector sinifi.
    Sadece ihtiyacim olanlari yapiyor. Ekstra tek ozellik yok.
    """

    __slots__ = ['x', 'y']

    def __init__(self, x_or_pair, y = None):
        if y == None:
            self.x = x_or_pair[0]
            self.y = x_or_pair[1]
        else:
            self.x = x_or_pair
            self.y = y

    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        raise IndexError("Invalid subscript.")

    def __add__(self, v):
        """Vektorel toplam."""
        return Vector(self.x+v[0], self.y+v[1])

    def __sub__(self, v):
        """Vektorel fark."""
        return Vector(self.x-v[0], self.y-v[1])

    def __mul__(self, r):
        """Vektorun bir skaler buyuklukle carpilmasi durumu."""
        return Vector(self[0]*r, self[1]*r)

    def __div__(self, r):
        """Vektorun bir skaler buyuklukle bolunmesi durumu."""
        return Vector(self[0]/r, self[1]/r)

    @property
    def length(self):
        """__len__ int dondurmek zorundaymis, boyle yaptim."""
        return sqrt(self.x**2 + self.y**2)

    def __repr__(self):
        return 'Vector(%s, %s)' % (self.x, self.y)

    def __str__(self):
        return '(%s, %s)' % (self.x, self.y)

    def dot_product(self, v):
        return self[0] * v[0] + self[1] * v[1]

    def cross_product(self, v):
        return Vector(self[0] * v[0], self[1] * v[1])

    def get_unit_vector(self):
        return Vector(self.x / self.length, self.y / self.length)

    def dik_vektor(self):
        return [[self[1], -self[0]], [-self[1], self[0]]]

def cross_product(v1, v2):
    return Vector(v1[0] * v2[0], v1[1] * v2[1])

def dot_product(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]

def get_unit_vector(v):
    return Vector(v[0], v[1]).get_unit_vector()

def r_vectorv(v, n):
    """Bir vektor ve carptigi yuzeyin normalini alir.
    Yansima vektorunu doner."""
    if type(v) != Vector:
        v = Vector(v)
    if type(n) != Vector:
        n = Vector(n)
    return v - (n*2*(v.dot_product(n))) 

if __name__ == "__main__":
    v1 = Vector(3, 5)
    print v1[0]
    print v1[1]
    v2 = Vector(10, 15)
    print v1 + v2
    print v1 - v2
    print v1 * 3
    print v1.length
    print v1.dot_product(v2)
    print v1.cross_product(v2)
    print v1.get_unit_vector()
    print r_vectorv([-1, -1], [-1, 0])
