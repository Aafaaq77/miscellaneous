# Uses python3
import sys

def get_majority_element(arr, left, right):
    arr_len = len(arr)
    count_dict = {}
    for element in arr:
        count_dict[str(element)] = count_dict.get(str(element), 0) + 1
        if count_dict[str(element)] > arr_len // 2:
            return 1
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
# test_list = [512766168, 717383758, 5, 126144732, 5, 573799007, 5, 5, 5, 405079772]
# print(get_majority_element(test_list, 0, 0))
