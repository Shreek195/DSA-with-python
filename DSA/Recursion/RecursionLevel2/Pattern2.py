def pattern(row, col):
    """
    *
    * *
    * * *
    * * * *
    """

    if row == 0:
        return

    if col < row:
        pattern(row, col+1)
        print("*", end=" ")

    if col == row:
        pattern(row-1, 0)
        print()


if __name__ == "__main__":
    pattern(4, 0)