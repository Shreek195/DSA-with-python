def search(arr, target):
    """
    :return [row_idx, col_idx]: if element is present, else: [-1, -1]
    :return -1: if array is empty
    """
    if len(arr) == 0:
        return -1

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == target:
                return [i, j]

    return [-1, -1]


if __name__ == "__main__":
    arr = [[1, 2, 3],
           [4, 5],
           [8, 9, 10]]
    target = 5

    print(search(arr, target))
