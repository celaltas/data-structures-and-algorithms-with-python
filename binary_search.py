def binary_search(arr, value):
    first_index = 0
    last_index = len(arr)-1
    flag = False

    while first_index <= last_index and not flag:
        middle_index = int((first_index+last_index)/2)
        if arr[middle_index] == value:
            flag = True
        else:
            if value < arr[middle_index]:
                last_index = middle_index - 1
            else:
                first_index = middle_index + 1
    return flag


arr = [3, 6, 11, 12, 18, 21, 34]


print(binary_search(arr, 15))


"""
Search in Rotated Array: Given a sorted array of n integers that has been rotated an unknown
number of times, write code to find an element in the array. You may assume that the array was
originally sorted in increasing order. Note: Either the left or right half must be normally ordered.
"""


def search(rotated_list, value, first_index=0, last_index=len(arr)-1):

    middle_index = int((first_index+last_index)/2)
    if value == rotated_list[middle_index]:
        return middle_index

    if last_index < first_index:
        return None

    if rotated_list[first_index] < rotated_list[middle_index]:  # left is normally ordered
        if value >= rotated_list[first_index and value < rotated_list[middle_index]]:
            return search(rotated_list, value, first_index=0, last_index=middle_index-1)
        else:
            return search(rotated_list, value, first_index=middle_index + 1, last_index=len(arr)-1)
    if rotated_list[first_index] > rotated_list[middle_index]:  # right is normally ordered
        if value > rotated_list[middle_index and value < rotated_list[last_index]]:
            return search(rotated_list, value, first_index=middle_index + 1, last_index=len(arr)-1)
        else:
            return search(rotated_list, value, first_index=0, last_index=middle_index-1)

    return None
