def is_prime(num):
    if num <= 1:
        return False

    c = 2
    while c ** 2 <= num:
        if num % c == 0:
            return False
        c += 1
    return True

if __name__ == '__main__':
    n = 20
    for i in range(2, n):
        print(f"{i} -> {is_prime(i)}")
