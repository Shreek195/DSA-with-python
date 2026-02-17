def pattern4(n):
    for r in range(n):
        for c in range(r + 1):
            print(c + 1, end='')
        print()


if __name__ == "__main__":
    pattern4(5)
