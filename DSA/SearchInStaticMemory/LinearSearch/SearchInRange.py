def linear_search(arr, target, start, end):
    """
    :return index if found the target in the given index range, else: return -1
    """
    if len(arr) == 0:
        return -1

    for i in range(start, end + 1):
        if arr[i] == target:
            return i

    return -1


if __name__ == "__main__":
    arr = [18, 12, -7, 3, 14, 28]
    target = 3231
    print(linear_search(arr, target, 1, 4))
