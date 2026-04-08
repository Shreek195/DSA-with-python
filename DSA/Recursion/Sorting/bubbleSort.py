def bubblesort(arr, row, col):
    if row == 0:
        return

    if col < row:
        # Swap
        if arr[col] > arr[col + 1]:
            arr[col], arr[col + 1] = arr[col + 1], arr[col]

        bubblesort(arr, row, col + 1)
    else:
        bubblesort(arr, row - 1, 0)



if __name__ == "__main__":
    arr = [4, 3, 2, 1]
    bubblesort(arr, len(arr) - 1, 0)

    print(arr)

