def merge_sort(arr):
    """
    This approach create a new array in each left and right sub-elements and merging.
    """
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[ :mid])
    right = merge_sort(arr[mid: ])

    return merge(left, right)

def merge(left, right):
    result = []

    k = i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        k += 1


    while i < len(left):
        result.append(left[i])
        i += 1
        k += 1

    while j < len(right):
        result.append(right[j])
        j += 1
        k += 1

    return result


if __name__ == "__main__":
    arr = [8, 3, 4, 12, 5, 6]

    print(merge_sort(arr))