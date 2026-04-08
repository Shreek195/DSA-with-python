def func(n):
    """
    5 4 3 2 1
    """
    if n == 0:
        return

    print(n)
    func(n - 1)


def funcRev(n):
    """
    1 2 3 4 5
    """
    if n == 0:
        return

    funcRev(n - 1)
    print(n)


def combined(n):
    """
    5 4 3 2 1 1 2 3 4 5
    """
    if n == 0:
        return

    print(n)
    combined(n - 1)
    print(n)



if __name__ == "__main__":
    # func(5)
    combined(5)