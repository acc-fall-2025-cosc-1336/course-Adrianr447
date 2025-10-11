#
def get_letter_grade(numerical_grade):
    """Return the letter grade for a given numerical grade using if/elif/else."""
    if 90 <= numerical_grade <= 100:
        return 'A'
    elif 80 <= numerical_grade <= 89:
        return 'B'
    elif 70 <= numerical_grade <= 79:
        return 'C'
    elif 60 <= numerical_grade <= 69:
        return 'D'
    elif 0 <= numerical_grade <= 59:
        return 'F'
    else:
        raise ValueError("Grade must be between 0 and 100.")

def get_letter_grade_switch(numerical_grade):
    """Return the letter grade using match/case (Python 3.10+) or if/elif fallback."""
    try:
        match numerical_grade:
            case grade if 90 <= grade <= 100:
                return 'A'
            case grade if 80 <= grade <= 89:
                return 'B'
            case grade if 70 <= grade <= 79:
                return 'C'
            case grade if 60 <= grade <= 69:
                return 'D'
            case grade if 0 <= grade <= 59:
                return 'F'
            case _:
                raise ValueError("Grade must be between 0 and 100.")
    except AttributeError:
        # Fallback for Python <3.10
        return get_letter_grade(numerical_grade)