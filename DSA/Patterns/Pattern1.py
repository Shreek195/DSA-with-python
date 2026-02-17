def pattern1(n):
    for _ in range(n):
        for _ in range(n):
            print("*", end='')
        print()


if __name__ == "__main__":
    pattern1(5)
