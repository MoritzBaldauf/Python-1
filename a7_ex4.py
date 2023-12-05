from a7_ex3 import Distance
class Minkowski(Distance):
    def __init__(self, x: int, vect1: list, vect2: list):
        super().__init__(x)
        self.vect1 = vect1
        self.vect2 = vect2

    def to_string(self) -> str:
        val_str = super().to_string()
        return str(f"{val_str}, vector_1={self.vect1}, vector_2={self.vect2}")
    def dist(self) -> float:
        distance = sum(abs(self.vect1[i] - self.vect2[i])**2 for i in range(len(self.vect1)))
        return round(distance**0.5,4)