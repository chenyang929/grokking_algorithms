def binary_search(lst, item):
    low = 0
    high = len(lst) - 1
    while low < high:
        mid = (low + high) // 2
        guess = lst[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid
    return 'Null'


if __name__ == '__main__':
    l = [2, 3, 5, 8, 11, 15]
    t1 = 8
    t2 = 9
    print(binary_search(l, t1))
    print(binary_search(l, t2))



