def main():
    arr = [[1, 2, [3]], 4]
    print(flatten(arr))
    arr2 = [[1, 2, 3], 4]
    print(flatten(arr2))
    arr3 = [[[1, 2, [3]], 4], 5]
    print(flatten(arr3))
    arr_empty = []
    print(flatten(arr_empty))
    arr_empty = [[1]]
    print(flatten(arr_empty))


def flatten(arr):
    return loop(arr, [])


def loop(arr, acc):
    for el in arr:
        if isinstance(el, list):
            acc + loop(el, acc)
        else:
            acc.append(el)
    return acc


if __name__ == "__main__":
    main()
