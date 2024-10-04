import stdarray

def rescale(array : list) -> list:
    """
    Rescale the values of the array to 0-1
    """
    min_val = min(array)
    max_val = max(array)
    return [(x - min_val) / (max_val - min_val) for x in array]

print(rescale([1, 2, 3, 4, 5]))


def histogram(array : list) -> list:
    """
    Create a histogram of the values in the array
    """
    hist = stdarray.create1D(6, 0)
    for i in array:
        hist[i] += 1
    return hist

print(histogram([1, 1, 1, 5, 5, 5, 5, 5]))