# O(n)
def factors(num):
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=' ')


if __name__ == "__main__":
    factors(20)
