"""List utility functions for HW07 (no built-in min/max)."""

def get_lowest_list_value(numbers):
    """Return the lowest value using a loop. Return None for empty list."""
    if not numbers:
        return None
    lowest = numbers[0]
    for num in numbers[1:]:
        if num < lowest:
            lowest = num
    return lowest

def get_highest_list_value(numbers):
    """Return the highest value using a loop. Return None for empty list."""
    if not numbers:
        return None
    highest = numbers[0]
    for num in numbers[1:]:
        if num > highest:
            highest = num
    return highest