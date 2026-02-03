def search(s, target):
    if len(s) == 0:
        return False

    for idx, ele in enumerate(s):
        if ele == target:
            return True

    return False


if __name__ == '__main__':
    s = "shree"
    target = 'e'

    print(search(s, target))
