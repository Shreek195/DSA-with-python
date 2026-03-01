def only_star(n):
    for _ in range(n):
        print("*", end='')


def pattern_random_1(n):
    for r in range(n + 1):
        space = n - r + 1
        for _ in range(space - 1):
            print(" ", end='')

        if r == 0 or r == n:
            only_star(n)
        else:
            print("*", end='')
            for k in range(n - 2):
                print(" ", end='')
            print("*", end='')

        print()


if __name__ == "__main__":
    pattern_random_1(5)
