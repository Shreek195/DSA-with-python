def find_unique(arr):
    """
    Here note array as only 1 unique and all others are occurring thrice

    We do here column-wise a bit addition of all the numbers in the array
    then as given all number appears thrice means they are multiple of 3
    so do '%' by 3, results will be binary bits of unique number

    finally we use result = 0, left shift << by 1 and do 'OR by resultant bit_count'

    0 | 0 = 0
    0 | 1 = 1
    1 | 0 = 1
    1 | 1 = 1


    as the result variable in not specified to store binary number, decimal will be displayed
    """
    bit_count = [0] * 4

    for num in arr:
        for i in range(3, -1, -1):
            bit_count[i] += num & 1
            num >>= 1

    for i in range(len(bit_count)):
        bit_count[i] %= 3

    result = 0
    for bit in bit_count:
        result = result << 1 | bit

    return result


if __name__ == "__main__":
    arr = [2, 2, 3, 2, 7, 7, 8, 7, 8, 8]
    print(find_unique(arr))
