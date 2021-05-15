# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 15:05:58 2021

@author: Aafaaq
"""

def merge_nums(right_list, left_list):
    #merge both by comparing elements
    #return final list
    sorted_list = []
    right, left = len(right_list), len(left_list)
    i, j = 0, 0
    while i < right and j < left:
        if right_list[i] <= left_list[j]:
            sorted_list.append(right_list[i])
            i += 1
        else:
            sorted_list.append(left_list[j])
            j += 1
    
    if right - i:
        sorted_list.extend(right_list[i:])
    else:
        sorted_list.extend(left_list[j:])
    return sorted_list


def merge_sort(nums_list):
    if len(nums_list) == 1:
        return nums_list
    right = merge_sort(nums_list[:len(nums_list)//2])
    left = merge_sort(nums_list[len(nums_list)//2:])
    return merge_nums(right, left)



nums = [12, 13, 9, 5, 10, 16, 11, 29, 1, 4, 3, 33, 18, 19, 20, 6]
print(merge_sort(nums))

