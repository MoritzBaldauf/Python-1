import numpy as np
import numbers

def extend(arr: np.ndarray, rows: int, cols: int, fill=None) -> np.ndarray:
    if arr.ndim != 2:
        raise ValueError(f"can only extend 2D arrays, not {arr.ndim}D")

    if rows < arr.shape[0]:
        raise ValueError("invalid rows")
    if cols < arr.shape[1]:
        raise ValueError("invalid cols")

    if fill is not None and not isinstance(fill, numbers.Number):
        raise ValueError("invalid fill")

    new_arr = np.empty((rows, cols), dtype=arr.dtype)

    new_arr[:arr.shape[0], :arr.shape[1]] = arr

    if fill is None:
        row_means = np.mean(arr, axis=1)
        col_means = np.mean(arr, axis=0)

        for i in range(arr.shape[0]):
            new_arr[i, arr.shape[1]:] = row_means[i]

        for j in range(arr.shape[1]):
            new_arr[arr.shape[0]:, j] = col_means[j]

        new_arr[arr.shape[0]:, arr.shape[1]:] = np.mean(arr)

    else:
        if rows > arr.shape[0]:
            new_arr[arr.shape[0]:, :] = fill
        if cols > arr.shape[1]:
            new_arr[:, arr.shape[1]:] = fill

    return new_arr

