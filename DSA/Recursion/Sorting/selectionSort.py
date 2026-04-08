def selection_sort(arr, row, col, max):
    if row == 0:
        return

    if col < row:
        if arr[col] > arr[max]:
            selection_sort(arr, row, col + 1, col)
        else:
            selection_sort(arr, row, col + 1, max)
    else:
        # Swap
        arr[max], arr[row - 1] = arr[row - 1], arr[max]
        selection_sort(arr, row - 1, 0, 0)



if __name__ == "__main__":
    arr = [111, 2, 3333, 3, 4, 111111]
    selection_sort(arr, len(arr) - 1, 0, 0)

    print(arr)

