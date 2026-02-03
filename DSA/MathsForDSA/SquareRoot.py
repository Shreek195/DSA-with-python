# O(log n)

def sqrt(num, fp):
    left, right = 0, num // 2

    root = 0.0
    while left <= right:
        mid = left + (right - left) // 2

        if mid ** 2 == num:
            root = mid
            break

        if mid ** 2 < num:
            # if we not get the value num, then take the floor value
            root = mid
            left = mid + 1
        else:
            right = mid - 1

    inc = 0.1
    for _ in range(fp):
        while root ** 2 <= num:
            root += inc
        root -= inc
        inc /= 10

    return root


if __name__ == '__main__':
    n = 36
    p = 0

    print(sqrt(n, p))
