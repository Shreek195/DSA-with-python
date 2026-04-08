def helper(arr, t, idx, result):
    if idx == len(arr):
        return result

    if arr[idx] == t:
        result.append(idx)

    return helper(arr, t, idx + 1, result)


def search_multiple_index(arr, t):
    result = helper(arr, t, 0, [])

    return result



if __name__ == "__main__":
    arr = [2, 3, 1, 4, 4, 5]
    t = 4
    print(search_multiple_index(arr, t))