import math


def find_number_of_digits(n, b):
    return int((math.log(n) / math.log(b)) + 1)


if __name__ == "__main__":
    num = 78903
    base = 10
    print(find_number_of_digits(num, base))
