def search(arr, target, s, e):
    if s > e:
        return -1

    mid = s + (e - s) // 2

    if target == arr[mid]:
        return mid

    if target > arr[mid]:
        return search(arr, target, mid + 1, e)
    return search(arr, target, s, mid - 1)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 55, 66, 78]
    target = 100

    print(search(nums, target, 0, len(nums) - 1))
