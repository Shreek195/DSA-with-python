def xor_range(a, b):
    return xor_zero_to_a(b) ^ xor_zero_to_a(a - 1)


def xor_zero_to_a(a):
    if a % 4 == 0:
        return a
    if a % 4 == 1:
        return 1

    if a % 4 == 2:
        return a + 1

    return 0


if __name__ == "__main__":
    a = 3
    b = 9
    print(xor_range(a, b))
