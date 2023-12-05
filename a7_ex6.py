from a7_ex4 import Minkowski
class Euclidean(Minkowski):
    def __init__(self, x: int, vect1: list, vect2: list):
        super().__init__(x, vect1, vect2)

    def to_string(self) -> str:
        return super().to_string()
    def dist(self) -> float:
        distance = sum((self.vect1[i] - self.vect2[i])**2 for i in range(len(self.vect1)))
        return round(distance**0.5, 4)

