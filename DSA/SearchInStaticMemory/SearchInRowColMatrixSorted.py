def search(matrix, target):
    """
    Search in the Sorted Matrix, here we try to reduce the search space
    TC: O(2n)
    """
    row, col = 0, len(matrix[0]) - 1

    while row < len(matrix) and col > -1:
        ele = matrix[row][col]

        if ele == target:
            return [row, col]

        if ele > target:
            col -= 1
        else:
            row += 1

    return [-1, -1]

if __name__ == "__main__":
    matrix = [[10, 20, 30, 40],
              [11, 25, 35, 45],
              [28, 29, 37, 49],
              [33, 34, 38, 50]]
    target = 38

    print(search(matrix, target))
