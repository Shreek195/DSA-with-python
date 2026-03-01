def fibo(n: int) -> int:
    # Base case: first two Fibonacci numbers
    if n < 2:
        return n

    # Recursive case:
    # Current value = sum of two smaller subproblems
    # (non-tail recursion: work happens after recursive calls return)
    return fibo(n - 1) + fibo(n - 2)


if __name__ == "__main__":
    print(fibo(4))
