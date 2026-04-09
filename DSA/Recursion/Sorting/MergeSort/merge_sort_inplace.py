def merge_sort_inplace(arr, s, e):
    # 1. BASE CASE: If the chunk is 1 element or less, it's already sorted
    if e - s <= 1:
        return

    mid = (s + e) // 2

    # Left half: from 's' up to (but not including) 'mid'
    merge_sort_inplace(arr, s, mid)
    # Right half: from 'mid' up to (but not including) 'e'
    merge_sort_inplace(arr, mid, e)

    merge_inplace(arr, s, mid, e)


def merge_inplace(arr, s, mid, e):
    mix = []

    i = s
    j = mid

    # 2 & 3. FIXED: Use append(), and append the correct variables
    while i < mid and j < e:
        if arr[i] <= arr[j]:  # <= keeps the sort stable for duplicate numbers
            mix.append(arr[i])
            i += 1
        else:
            mix.append(arr[j])
            j += 1

    # Add any remaining elements from the left side
    while i < mid:
        mix.append(arr[i])
        i += 1

    # 4. FIXED: Add remaining elements from the right side (up to 'e', not 'mid')
    while j < e:
        mix.append(arr[j])
        j += 1

    # Copy the sorted 'mix' back into the original array
    for l in range(len(mix)):
        arr[s + l] = mix[l]


if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]

    # Pass len(arr) as the exclusive end bound (5 instead of 4)
    # This makes the math inside the functions much cleaner!
    merge_sort_inplace(arr, 0, len(arr))

    print(arr)