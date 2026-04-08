def helper(arr, t, idx):
    curr_lst = []

    if idx == len(arr):
        return curr_lst

    if arr[idx] == t:
        curr_lst.append(idx)

    get_ans_lst = helper(arr, t, idx + 1)
    get_ans_lst.extend(curr_lst)

    return get_ans_lst


def search_multiple_index(arr, t):
    result = helper(arr, t, 0)

    return result


if __name__ == "__main__":
    arr = [2, 3, 1, 4, 4, 5]
    t = 4
    print(search_multiple_index(arr, t))
