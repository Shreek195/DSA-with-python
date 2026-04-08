def search(arr, t, idx):
    if idx == len(arr):
        return False

    return arr[idx] == t or search(arr, t, idx + 1)


def search_idx(arr, t, idx):
    if idx == len(arr):
        return -1

    if arr[idx] == t:
        return idx
    return search_idx(arr, t, idx + 1)


def search_index_last(arr, t, idx):
    if idx == -1:
        return -1

    if arr[idx] == t:
        return idx
    return search_index_last(arr, t, idx - 1)


if __name__ == "__main__":
    arr = [3, 2, 1, 18, 9]
    t = 18

    print(search(arr, t, 0))
    print(search_idx(arr, t, 0))
    print(search_index_last(arr, t, len(arr) - 1))
