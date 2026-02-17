def pattern3(n):
    for r in range(n, -1, -1):
        for _ in range(r + 1):
            print("*", end='')
        print()


if __name__ == "__main__":
    pattern3(4)
