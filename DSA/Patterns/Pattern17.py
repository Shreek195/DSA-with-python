def pattern17(n):
    for row in range(n * 2):
        c = 2 * n - row if row > n else row

        # spaces
        for space in range(n - c):
            print("  ", end="")

        # increasing
        for col in range(c, 0, -1):
            print(col, end=" ")

        # decreasing
        for col in range(2, c + 1):
            print(col, end=" ")

        print()


if __name__ == "__main__":
    pattern17(5)
