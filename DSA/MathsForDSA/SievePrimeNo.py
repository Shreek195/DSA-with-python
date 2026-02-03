def sieve(n):
    prime_lst = [True] * (n + 1)
    prime_lst[0] = prime_lst[1] = False

    for c in range(2, int(n ** 0.5) + 1):
        if prime_lst[c]:
            for j in range(c * c, n + 1, c):
                prime_lst[j] = False

    return prime_lst


if __name__ == '__main__':
    num = 40
    for idx, ele in enumerate(sieve(num)):
        if ele:
            print(idx)
