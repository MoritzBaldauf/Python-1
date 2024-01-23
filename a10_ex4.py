import numpy as np

def moving_average_2D(arr: np.ndarray, size: int) -> np.ndarray:
    if arr.ndim != 2:
        raise ValueError(f"apply for 2D array, not {arr.ndim}D")

    if not np.issubdtype(arr.dtype, np.number):
        raise TypeError("Invalid data type")

    if size < 1 or size > arr.shape[0] or size > arr.shape[1]:
        raise ValueError("Invalid window size")

    nr, nc = arr.shape
    result_shape = (nr - size + 1, nc - size + 1)
    result = np.zeros(result_shape, dtype=float)

    for i in range(result_shape[0]):
        for j in range(result_shape[1]):
            result[i, j] = np.mean(arr[i:i+size, j:j+size])

    return result
