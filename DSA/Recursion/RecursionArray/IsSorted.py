def is_sorted(arr, idx):
    if idx == len(arr) - 1:
        return True

    return arr[idx] < arr[idx + 1] and is_sorted(arr, idx + 1)


if __name__ == "__main__":
    arr = [1, 2, 4, 5, 9, 12]

    print(is_sorted(arr, 0))