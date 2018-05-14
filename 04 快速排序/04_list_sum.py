# 常规数组求和，遍历求和
def list_sum_1(lst):
    total = 0
    for item in lst:
        total += item
    return total


# 递归法
def list_sum_2(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + list_sum_2(lst[1:])


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5]
    print(list_sum_1(l))
    print(list_sum_2(l))
