def binary_search(mat, target, col_s, col_e, row):
    """
    Performs binary search on a specific row between given column bounds.
    Returns [row, col] if target is found, else [-1, -1].
    """
    while col_s <= col_e:
        mid = col_s + (col_e - col_s) // 2

        if mat[row][mid] == target:
            return [row, mid]

        if mat[row][mid] < target:
            col_s = mid + 1
        else:
            col_e = mid - 1

    return [-1, -1]


def search(matrix, target):
    """
    Searches for target in a strictly sorted 2D matrix.

    Strategy:
    1. Use binary search on rows to reduce the search space to 2 candidate rows.
    2. Check the middle column of those rows.
    3. Based on comparisons, divide into 4 possible sub-parts.
    4. Perform binary search on the appropriate part.
    """

    col_s, col_e = 0, len(matrix[0]) - 1
    row_s, row_e = 0, len(matrix) - 1

    # If only one row exists, perform normal binary search on that row
    if row_e == 0:
        return binary_search(matrix, target, col_s, col_e, 0)

    # Step 1: Reduce rows to 2 possible candidate rows
    col_mid = col_s + (col_e - col_s) // 2  # Fix a middle column

    while row_s < row_e - 1:
        # Continue until only 2 rows remain
        row_mid = row_s + (row_e - row_s) // 2

        if matrix[row_mid][col_mid] == target:
            return [row_mid, col_mid]

        if matrix[row_mid][col_mid] < target:
            # Target must be in lower half
            row_s = row_mid
        else:
            # Target must be in upper half
            row_e = row_mid

    # Now only 2 rows remain: row_s and row_e

    # Case 1: Target is in left half of row_s
    if matrix[row_s][col_mid] > target:
        return binary_search(matrix, target, 0, col_mid - 1, row_s)

    # Case 2: Target is in right half of row_s
    if matrix[row_s][col_mid] < target <= matrix[row_s][col_e]:
        return binary_search(matrix, target, col_mid, col_e, row_s)

    # Case 3: Target is in left half of row_e
    if matrix[row_e][col_mid] > target:
        return binary_search(matrix, target, 0, col_mid - 1, row_e)

    # Case 4: Target is in right half of row_e
    return binary_search(matrix, target, col_mid, col_e, row_e)


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]

    target = 3
    print(search(matrix, target))
