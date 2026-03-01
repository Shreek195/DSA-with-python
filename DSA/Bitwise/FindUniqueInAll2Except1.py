def find_unique(arr):
    """
    Here note array as only 1 unique and all others are occurring twice

    Because XOR has the properties:
    1. a^1 = ~a
    2. a^0 = a
    3. a^a = 0

    Here we used the 3rd property
    """
    unique = 0
    for i in arr:
        unique ^= i

    return unique


if __name__ == "__main__":
    arr = [2, 3, 3, 4, 2, 6, 4]
    print(find_unique(arr))
