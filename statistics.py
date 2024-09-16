"""Statistics operation functions."""
from math import sqrt, nan


def average(data):
    """Return the average of a list of numeric values in data.

    :param data: List of numeric values.
    :raises ValueError: If the list is empty.
    :returns: The average of the numeric values in data.

    >>> average([1, 2, 3])
    2.0
    >>> average([5, 5, 5])
    5.0
    >>> average([])
    Traceback (most recent call last):
        ...
    ValueError: List must contain at least one value
    """
    if nan in data:
        raise TypeError
    if len(data) == 0:
        raise ValueError("List must contain at least one value")
    return sum(data) / len(data)


def variance(data):
    """Return the variance of the data in the list.

    The variance is the sum of squared differences between data values
    and their mean, divided by the number of items in the list.
    This is different from the Python library function statistics.variance
    which returns the sample variance, where the sum is divided by (n-1).

    :param data: List of numbers for which variance will be computed.
    :raises ValueError: If the list is empty.
    :returns: Population variance of values in data list.

    >>> variance([1])
    0.0
    >>> variance([1, 1, 1, 1])
    0.0
    >>> variance([1, 2])
    0.25
    >>> variance([1000000, 1000004])
    4.0
    >>> variance([])
    Traceback (most recent call last):
        ...
    ValueError: List must contain at least one value
    """
    n = len(data)
    if nan in data:
        raise TypeError
    if n == 0:
        raise ValueError("List must contain at least one value")

    avg = average(data)

    # Calculate variance using population formula
    var = sum((x - avg) ** 2 for x in data) / n
    return var


def stdev(data):
    """Return standard deviation of the list.

    :param data: List of numbers for which standard deviation will be computed.
    :raises ValueError: If the list is empty.

    >>> stdev([10.0])
    0.0
    >>> stdev([1, 5])
    2.0
    >>> stdev([])
    Traceback (most recent call last):
        ...
    ValueError: List must contain at least one value
    """
    if nan in data:
        raise TypeError
    if len(data) <= 0:
        raise ValueError("List must contain at least one value")

    return sqrt(variance(data))
