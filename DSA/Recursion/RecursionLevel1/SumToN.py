def sum_to_n(n):
    if n <= 1:
        return 1

    return n + sum_to_n(n - 1)


if __name__ == "__main__":
    print(sum_to_n(7))