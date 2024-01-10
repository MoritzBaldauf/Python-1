
class Power:
    def __init__(self, exponent):
        if type(exponent) is int or type(exponent) is float:
            self.exponent = exponent
        else:
            raise TypeError("The exponent must be a numerical value.")

    def __call__(self, x):
        if type(x) is int or type(x) is float:
            power = x ** self.exponent
            return power
        else:
            raise TypeError("Input must be a numerical value.")

    def __mul__(self, other):
        if type(other) is int or type(other) is float:
            new_exponent = self.exponent + other
            return Power(new_exponent)
        elif isinstance(other, Power):
            new_exponent = self.exponent + other.exponent
            return Power(new_exponent)
        else:
            return NotImplemented

class Square(Power):
    def __init__(self):
        self.exponent = 2
