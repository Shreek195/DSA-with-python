def selection_sort(arr):
    """
    I choose to select max element, we can also go with selecting min element
    and swapping it with the first index of the array
    """

    # Traverse the array n-1 times
    # After each pass, the largest element from the unsorted portion
    # is placed at its correct position at the end.
    for i in range(len(arr) - 1):

        # Assume the first element in the unsorted portion is the maximum
        max_ele = 0

        # Search for the maximum element in the unsorted portion
        # The last i elements are already sorted, so ignore them
        for j in range(1, len(arr) - i):
            if arr[j] > arr[max_ele]:
                max_ele = j

        # Swap the found maximum element
        # with the last element of the unsorted portion
        arr[max_ele], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[max_ele]

    return arr


if __name__ == "__main__":
    nums = [2, -32, 0, 78, 1]
    print(selection_sort(nums))
