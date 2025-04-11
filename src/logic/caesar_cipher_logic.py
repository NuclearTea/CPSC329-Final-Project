import string

def caesar_cipher(msg: string, shift: int, en_de: int) -> string:
    """Apply and return the encoded/decoded message"""

    # If we are decoding, negate the shift value
    # en_de value of [0] is encoding, [1] is decoding
    if(en_de == 1):
        shift = shift * -1
    
    # Define uppercase and lowercase alphabets to use for shifting
    alpha_upper: list = list(string.ascii_uppercase)
    alpha_lower: list = list(string.ascii_lowercase)

    # Define list we are using to append shifted characters to
    new_msg: list = []

    # Main loop for shifting and appending shifted characters 
    for i in range(len(msg)):
        index = 0
        character = msg[i]
    
        # If the next characrer is not a letter, just append it
        if(character == ' ' or character.isalpha() == False):
            new_msg.append(character)
        
        # Otherwise, apply the shift and then append it
        else:

            # Choose the appropriate alphabet list depending on case
            if(character.islower()):
               alpha = alpha_lower
            if(character.isupper()):
               alpha = alpha_upper

            # Find the index of the character to shift
            while(character != alpha[index] and index < len(alpha) - 1):
               index = index + 1
    

            # Get the new index from applying the shift
            new_index = len(alpha) + index + shift

            # If we must loop around the alphabet, update the new index accordingly
            while(new_index > len(alpha) - 1):
               new_index = new_index - len(alpha)
            
            # Append shifted character to the string we want to return
            new_msg.append(alpha[new_index])


    # Return the resultant encoded/decoded string 
    return ''.join(new_msg)


def handle_shift(shift: string) -> int:
    """Handling the shift input"""

    # Checking if shift input is potentially a negative number
    # First see if the shit input starts with '-'

    # To flag pos/neg values
    is_negative = False

    if shift.startswith('-'):
        # Remove the '-' to see if the resultant value is a number
        shift = list(shift)
        shift.remove('-')
        shift = ''.join(shift)

        # Flag the negative
        # This will only be used if the rest is numeric
        is_negative = True

    # Checking if the shift input is numeric
    if shift.isnumeric():
        # Cast to int if so
        shift = int(shift)

        # If we flagged the negative, add it back
        if(is_negative):
            shift = shift * -1

    # Shift value is not numeric so return a 0
    else:
        # No shifting for people who don't listen
        shift = 0


    return shift

