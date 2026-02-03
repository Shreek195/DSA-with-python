def floor_value(arr, target):
    """
    Returns the index as 'end' if target is not present in the array, else target index
    if 'end' goes out of bound on the left-end return -1
    """

    # pointers
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if target == arr[mid]:
            return mid

        if target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return end


if __name__ == "__main__":
    arr = [2, 3, 5, 9, 14, 16, 18]
    target = 4

    print(floor_value(arr, target))
