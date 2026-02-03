def linear_search(arr, target):
    """
    :returns the index of the target element using linear search,
    else: returns garbage value

    NOTE: Python integers are unbounded, so there is no maximum value.
    We typically use float('inf') or a large sentinel value depending on the problem.

    OR else, simply use True or False
    """
    if len(arr) == 0:
        return float('inf')

    for idx, ele in enumerate(arr):
        if ele == target:
            return idx

    return float('inf')


if __name__ == '__main__':
    arr = [25, 45, 1, 2, 8, 19, -3, 16, -11, 28]
    target = 20
    ans = linear_search(arr, target)
    print(ans)
