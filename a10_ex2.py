import numpy as np
def elements_wise(arr: np.ndarray, f):
    it = np.nditer(arr, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        arr[it.multi_index] = f(arr[it.multi_index])
        it.iternext()

