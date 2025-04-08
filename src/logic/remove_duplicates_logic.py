def remove_duplicates(input_string, chars_to_remove):
    """Remove specified characters from the input string."""
    return ''.join(char for char in input_string if char not in chars_to_remove)

def duplicate_characters(input_string, chars_to_duplicate):
    """Duplicate specified characters in the input string."""
    result = []
    for char in input_string:
        result.append(char)
        if char in chars_to_duplicate:
            result.append(char)  # Duplicate the character
    return ''.join(result)