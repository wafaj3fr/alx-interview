#!/usr/bin/python3
"""UTF-8 Validation"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    :param data: List of integers
    :return: True if data is a valid UTF-8 encoding, else return False
    """
    number_of_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        mask = 1 << 7
        if number_of_bytes == 0:
            # Determine how many bytes in the current UTF-8 character
            while mask & num:
                number_of_bytes += 1
                mask >>= 1

            # 1-byte character
            if number_of_bytes == 0:
                continue

            # UTF-8 characters are 1 to 4 bytes long
            if number_of_bytes == 1 or number_of_bytes > 4:
                return False
        else:
            # Check that the remaining bytes are of the form 10xxxxxx
            if not (num & mask1 and not (num & mask2)):
                return False

        number_of_bytes -= 1

    return number_of_bytes == 0

