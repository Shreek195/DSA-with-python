def pattern2(n):
    for r in range(n):
        for _ in range(r + 1):
            print("*", end='')
        print()


if __name__ == "__main__":
    pattern2(4)
