def find_magic_number(n):
    """
    Magic number:
    n = 6, 0110
    From LSB to MSB
    (5**4) * 0 + (5**3) * 1 + (5**2) * 1 + (5**1) * 0

    in code, we can use 'n & 1' bitwise to get the LSB, then left shit >> the n by 1
    """
    result = 0

    base = 5
    while n > 0:
        last_bit = n & 1
        n >>= 1
        result += last_bit * base
        base *= 5

    return result


if __name__ == "__main__":
    n = 6
    print(find_magic_number(n))
