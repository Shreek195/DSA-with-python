def recur1(n: int) -> None:
    # Base case: stop when n reaches 5
    if n == 5:
        print(n)
        return

    # Work before recursive call (pre-order action)
    print(n)

    # Recursive call with smaller/bigger subproblem
    recur1(n + 1)


if __name__ == "__main__":
    recur1(1)
