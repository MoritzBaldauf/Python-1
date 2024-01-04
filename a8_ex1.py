import math

class Angle:
    def __init__(self, degree: float = None, radian: float = None):
        self.degree = degree
        self.radian = radian

        if degree is not None and radian is not None:
            self.degree = degree
            self.radian = radian
            self.consistency()
        elif degree is not None:
            self.radian = self.deg_to_rad(degree)
        elif radian is not None:
            self.degree = self.rad_to_deg(radian)
        else:
            raise ValueError("Either degree or radian must be specified.")

    def consistency(self):
        if not math.isclose(self.radian, self.deg_to_rad(self.degree)):
            raise ValueError("Degree and radian are not consistent.")

    def __eq__(self, other):
        if not isinstance(other, Angle):
            return NotImplemented
        return math.isclose(self.degree, other.degree) and math.isclose(self.radian, other.radian)

    def __repr__(self):
        return f"Angle(degree={self.degree:.3f}, radian={self.radian:.3f})"

    def __str__(self):
        return f"{self.degree:.2f} deg = {self.radian:.2f} rad"

    def __add__(self, other):
        if isinstance(other, Angle):
            added_degree = self.degree + other.degree
            added_radian = self.radian + other.radian
            return Angle(added_degree, added_radian)
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Angle):
            self.degree += other.degree
            self.radian += other.radian
            self.consistency()
            return self
        else:
            return NotImplemented

    @staticmethod
    def deg_to_rad(degree):
        return degree * (math.pi / 180)

    @staticmethod
    def rad_to_deg(radian):
        return radian * (180 / math.pi)

    @staticmethod
    def add_all(angle: 'Angle', *angles: 'Angle'):
        sum_angle = angle
        for i in angles:
            sum_angle += i
        return sum_angle

# Your example execution
a1 = Angle(degree=45)
a2 = Angle(radian=math.pi/4)
a3 = Angle(30, math.pi/6)
print(a1)
print(a2.__repr__())
print(repr(a3))
print(a1 == a2)
print(a1 + a2)
a1 += a3
print(a1)
sum_angle = Angle.add_all(a1, a2, a3)
print(sum_angle)
try:
    a4 = Angle()
except ValueError as e:
    print(e)
try:
    a5 = Angle(degree=45, radian=1)
except ValueError as e:
    print(e)