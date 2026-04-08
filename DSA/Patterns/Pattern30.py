def pattern30(n):

    for row in range(n):
        # spaces
        for space in range(n - row):
            print("  ", end="")

        # decreasing numbers
        for col in range(row + 1, 0, -1):
            print(col, end=" ")

        # increasing numbers
        for col in range(2, row + 2):
            print(col, end=" ")

        print()


if __name__ == "__main__":
    pattern30(5)
