"""Combined HW07 + HW08 list utilities (loops only)."""

def get_lowest_list_value(numbers):
    """Return lowest value in numbers using a loop. Return None for empty input."""
    if not numbers:
        return None
    # assume numbers is a list-like sequence
    lowest = numbers[0]
    i = 1
    while i < len(numbers):
        if numbers[i] < lowest:
            lowest = numbers[i]
        i += 1
    return lowest


def get_highest_list_value(numbers):
    """Return highest value in numbers using a loop. Return None for empty input."""
    if not numbers:
        return None
    highest = numbers[0]
    i = 1
    while i < len(numbers):
        if numbers[i] > highest:
            highest = numbers[i]
        i += 1
    return highest


def get_p_distance(list1, list2):
    """
    p-distance = (# of positions where list1[i] != list2[i]) / length
    Precondition: list1 and list2 must be the same length (> 0).
    Returns a float rounded to 1 decimal place.
    """
    if list1 is None or list2 is None:
        raise ValueError("Inputs cannot be None")
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Inputs must be lists")
    if len(list1) != len(list2) or len(list1) == 0:
        raise ValueError("Lists must be same non-zero length")

    mismatches = 0
    length = len(list1)

    i = 0
    while i < length:
        if list1[i] != list2[i]:
            mismatches += 1
        i += 1

    return round(mismatches / length, 1)


def get_p_distance_matrix(lists_of_dna):
    """
    Given a list of equal-length DNA lists, return the NxN p-distance matrix.
    Values rounded to 1 decimal.
    """
    if lists_of_dna is None or not isinstance(lists_of_dna, list) or len(lists_of_dna) == 0:
        raise ValueError("Must provide a non-empty list of DNA lists")

    n = len(lists_of_dna)
    row_len = len(lists_of_dna[0])
    if row_len == 0:
        raise ValueError("DNA strings must have positive length")

    idx = 1
    while idx < n:
        if len(lists_of_dna[idx]) != row_len:
            raise ValueError("All DNA lists must be the same length")
        idx += 1

    matrix = []
    i = 0
    while i < n:
        row = []
        j = 0
        while j < n:
            if i == j:
                row.append(0.0)
            else:
                row.append(get_p_distance(lists_of_dna[i], lists_of_dna[j]))
            j += 1
        matrix.append(row)
        i += 1

    return matrix