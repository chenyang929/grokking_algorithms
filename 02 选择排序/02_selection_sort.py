def find_smallest(lst):
    smallest_index = 0
    smallest_item = lst[0]
    for i in range(1, len(lst)):
        if smallest_item > lst[i]:
            smallest_item = lst[i]
            smallest_index = i
    return smallest_index


def selection_sort(lst):
    new_lst = []
    for i in range(len(lst)):
        small_index = find_smallest(lst)
        new_lst.append(lst.pop(small_index))
    return new_lst


if __name__ == '__main__':
    print(selection_sort([4, 9, 7, 5, 3, 8]))
