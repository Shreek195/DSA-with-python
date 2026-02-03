import math


# O(srqt(n))
# def factors(num):
#     for i in range(1, int(math.sqrt(num) + 1)):
#         if num % i == 0:
#             if num / i == i:
#                 print(i, end=' ')
#             else:
#                 print(f"{i} {num // i}", end=' ')

# Sorting the Answer
def factors2(num):
    lst = []

    for i in range(1, int(math.sqrt(num) + 1)):
        if num % i == 0:
            if num / i == i:
                print(i, end=' ')
            else:
                print(f"{i}", end=' ')
                # Store the n / i in list
                lst.append(num // i)


    # list will store the value in descending order based on the logic
    for i in range(len(lst)-1, -1, -1):
        print(lst[i], end=' ')


if __name__ == "__main__":
    # factors(20)
    factors2(36)
