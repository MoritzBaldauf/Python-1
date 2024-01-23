import numpy as np

def one_hot_encoding(arr: np.ndarray) -> np.ndarray:
    if arr.ndim != 1:
        raise ValueError(f"The function can work for 1D matrices, not {arr.ndim}D")

    unique_elements = np.sort(np.unique(arr))

    element_to_index = {element: index for index, element in enumerate(unique_elements)}

    encoded_array = np.zeros((len(arr), len(unique_elements)))

    for i, element in enumerate(arr):
        encoded_array[i, element_to_index[element]] = 1

    return encoded_array

