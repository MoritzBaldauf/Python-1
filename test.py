from a7_ex3 import Distance
from a7_ex4 import Minkowski
from a7_ex5 import Manhattan
from a7_ex6 import Euclidean

vect1 = [1,2,3]
vect2 = [4,5,6]
d = Distance(2)
print(d.to_string())
try:
    d.dist()
except NotImplementedError:
    print("NotImplementedError")

k = Minkowski(2, vect1, vect2)
print(k.to_string())
print("Minkowski distance: ", k.dist())

m = Manhattan(2, vect1, vect2)
print(m.to_string())
print("Manhattan distance: ", m.dist())

e = Euclidean(2, vect1, vect2)
print(e.to_string())
print("Euclidean distance: ", e.dist())
