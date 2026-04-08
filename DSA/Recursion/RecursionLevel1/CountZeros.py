def func(n, c):
    if n % 10 == n:
        return c

    if n % 10 == 0:
        return func(n // 10, c + 1)

    return func(n // 10, c)


def count_zeros(n):
    return func(n, 0)


if __name__ == "__main__":
    print(count_zeros(1001))
