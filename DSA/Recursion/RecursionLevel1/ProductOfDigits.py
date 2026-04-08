def prod_of_digits(n):
    if n % 10 == n:
        return n

    return (n % 10) * prod_of_digits(n // 10)


if __name__ == "__main__":
    print(prod_of_digits(1230456789))
