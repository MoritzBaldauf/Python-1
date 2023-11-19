#f(5) -> h1 h2 g1 f1 f3
#f(-5) -> h1 h2 g3 g5 g6 f1 f3
#f(11) -> h1 g1 g2 f1 f2 f3
#f(-11) -> h1 h2 g1 h3 g4 g6 f3

def f(x: int):
    try:
        g(x)
        print("f1")
    except ValueError:
        print("f2")
    finally:
        print("f3")
def g(x: int):
    try:
        h(x)
        print("g1")
    except ValueError: # Error A
        print("g2")
    except TypeError: # Error B
        print("g3")
        if x < -10:
            raise TimeoutError # Error C
            print("g4")
        else:
            print("g5")
        print("g6")
def h(x: int):
    try:
        if x > 10:
            raise ValueError
        if x < 0:
            raise TypeError
    finally:
            print("h1")
    print("h2")
f(- 11)