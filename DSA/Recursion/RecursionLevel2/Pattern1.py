def pattern(row, col):
    """
    * * * *
    * * *
    * *
    *
    """

    if row == 0:
        return

    if col < row:
        print("*", end=" ")
        pattern(row, col + 1)

    if row == col:
        print()
        pattern(row - 1, 0)


if __name__ == "__main__":
    pattern(5, 0)