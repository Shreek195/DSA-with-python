def power_calc(b, p):
    ans = 1

    while p > 0:
        if (p & 1) == 1:
            ans *= b

        b *= b
        p >>= 1

    return ans


if __name__ == "__main__":
    base = 3
    power = 6
    print(power_calc(base, power))
