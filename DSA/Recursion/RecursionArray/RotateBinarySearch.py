def binary_search(arr, t, start, end):
    if start > end:
        return -1

    mid = (end + start) // 2

    if arr[mid] == t:
        return mid

    if arr[start] <= arr[mid]:
        if arr[start] <= t <= arr[mid]:
            end = mid - 1
            return binary_search(arr, t, start, end)
        else:
            start = mid + 1
            return binary_search(arr, t, start, end)

    if arr[mid] <= t <= arr[end]:
        start = mid + 1
        return binary_search(arr, t, start, end)

    end = mid - 1
    return binary_search(arr, t, start, end)


if __name__ == "__main__":
    arr = [5, 6, 7, 8, 9, 1, 2, 3]

    print(binary_search(arr, 8, 0, len(arr) - 1))