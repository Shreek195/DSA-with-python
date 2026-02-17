def pattern5(n):
    for r in range(n * 2):
        if r > n:
            c = (2 * n) - r
        else:
            c = r

        for _ in range(c):
            print("*", end='')

        print()


if __name__ == "__main__":
    pattern5(4)
