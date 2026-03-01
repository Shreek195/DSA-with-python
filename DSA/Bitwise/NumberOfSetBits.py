def set_bits(n):
    count = 0

    while n > 0:
        count += 1
        n -= (n & -n)  # or n = n & (n - 1)

    return count


if __name__ == "__main__":
    n = 16
    print(set_bits(n))
