def remove_duplicates(input_string, chars_to_remove):
    """Remove specified characters from the input string."""
    return ''.join(char for char in input_string if char not in chars_to_remove)

