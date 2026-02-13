def count_sort(arr):
    # It works when elements are in the range 1 to n.

    i = 0

    # Iterate through the array
    while i < len(arr):

        # Calculate the index where the current element should be
        # Since numbers are 1-based, correct index = value - 1
        correct_idx = arr[i] - 1

        # If the current element is already at its correct position,
        # move to the next index
        if i == correct_idx:
            i += 1
        else:
            # Otherwise, swap it with the element at its correct index
            # This places at least one element in its correct position
            arr[i], arr[correct_idx] = arr[correct_idx], arr[i]

    return arr


if __name__ == "__main__":
    nums = [3, 5, 2, 1, 4]
    print(count_sort(nums))
