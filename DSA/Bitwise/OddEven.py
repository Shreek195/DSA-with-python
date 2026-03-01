def is_odd(n):
    """
    Here, 'Bitwise &' will do the '&' operation on the LSB of the number
    that LSB is the only one Bit in the whole number that can be 1 (odd) or 0 (even)

    because other bits than LSB are always 2 power n, resulting to even numbers

    Ex:
    0000 = 0
    0001 = 1
    0010 = 2
    0011 = 3
    0100 = 4
    0101 = 5
    .
    .
    .
    """
    return n & 1 == 1

if __name__ == "__main__":
    n = 100
    print(is_odd(n))