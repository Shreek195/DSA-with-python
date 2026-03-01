def is_power_of_2(n):
    if n == 0:
        return False
    return n & (n - 1) == 0


if __name__ == "__main__":
    n = 1024
    print(is_power_of_2(n))
