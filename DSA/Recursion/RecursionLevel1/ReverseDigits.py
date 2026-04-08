import math


def func(n, p):
    if n % 10 == n:
        return (n % 10) * (10 ** p)

    return (n % 10) * (10 ** p) + func(n // 10, p - 1)


def reverse_digits(n):
    p = int(math.log10(n))

    return func(n, p)


if __name__ == "__main__":
    print(reverse_digits(12345))
