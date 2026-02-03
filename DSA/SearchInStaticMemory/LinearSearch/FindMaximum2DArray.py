def max_ele(arr):
    """
    Returns:
        int: Maximum element in the 2D array, or -1 if empty.

    Note:
        float('-inf') is used to correctly compare negative values.
    """

    if len(arr) == 0:
        return -1

    ans = float('-inf')
    for ele in arr:
        for j in ele:
            if j > ans:
                ans = j

    return ans


if __name__ == "__main__":
    arr = [[1, 2, 3],
           [4, 5],
           [8, 9, 10]]

    print(max_ele(arr))
