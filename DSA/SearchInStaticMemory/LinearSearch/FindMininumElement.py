def find_min(arr):
    """
    :return index, if found the minimum element else: -1 for the empty array
    """
    if len(arr) == 0:
        return -1

    ans = arr[0]
    for idx, ele in enumerate(arr):
        if ele < ans:
            ans = ele

    return ans


if __name__ == "__main__":
    arr = [18, 12, 7, 3, 14, 28]
    print(find_min(arr))
