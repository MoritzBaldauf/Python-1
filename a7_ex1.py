class Radian:
    def __init__(self, degree: float):
        self.degree = degree

    def rad(self):
        radiant = (self.degree * (3.14 / 180.0))
        radiant_return = f"{radiant:.2f}"
        return radiant_return

    def print(self):
        degree = self.degree
        radiant = self.rad()
        print(f"The degree is {degree:.2f} and the radian is {radiant}")


c = Radian(180)
print(c.rad())
c.print()
