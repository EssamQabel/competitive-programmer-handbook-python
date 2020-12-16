# Bubble Sort O(n^2)
arr = [1, 3, 8, 2, 9, 2, 5, 6]
for i, j in enumerate(arr):
    for a, b in enumerate(arr[:-1]):
        if arr[a] > arr[a + 1]:
            arr[a], arr[a + 1] = arr[a + 1], arr[a]
print(arr)

# Merge Sort O(nlogn)- implementation is OPTIONAL
arr = [1, 3, 8, 2, 9, 2, 5, 6]
def merge_sort(array, left_index=None, right_index=None):
    if left_index is None: left_index = 0
    if right_index is None: right_index = len(array)-1
    if left_index >= right_index:
        return

    middle = (left_index + right_index)//2
    merge_sort(array, left_index, middle)
    merge_sort(array, middle + 1, right_index)
    merge(array, left_index, right_index, middle)

def merge(array, left_index, right_index, middle):
    left_copy = array[left_index:middle + 1]
    right_copy = array[middle+1:right_index+1]
    
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1

    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1
merge_sort(arr)       
print(arr)

# Counting Sort O(n) - implementation is OPTIONAL
arr = [1, 3, 6, 9, 9, 3, 5, 9]
def counting_sort(arr):
    N = max(arr)
    count_arr = [0] * (N+1)
    for i in arr: count_arr[i] += 1
    
    sorted_arr = []
    for i in range(1, N+1):
        for j in range(count_arr[i]):
            sorted_arr.append(i)
        
    return sorted_arr

sorted_arr = counting_sort(arr)
print(sorted_arr)

# Sorting functions in Python
arr = [1, 3, 8, 2, 9, 2, 5, 6]
print(sorted(arr), arr)
print(arr.sort(), arr)

# Binary Search
arr = [1, 2, 2, 3, 5, 6, 8, 9]

def binary_search(arr, elem, prim_index=0):
    mid = int(len(arr) / 2)
    mid_elem = arr[mid]
    if len(arr) == 1 and elem != mid_elem:
        return -1
    if mid_elem == elem:
        return mid + prim_index
    if mid_elem > elem:
        return binary_search(arr[:mid], elem, prim_index)
    if mid_elem < elem:
        return binary_search(arr[mid:], elem, prim_index + mid)

# Array must be sorted first, before using binary search
sorted_arr = counting_sort(arr)

print(binary_search(sorted_arr, 9))
print(binary_search(sorted_arr, 5))
print(binary_search(sorted_arr, 3))

# Upper Bound and Lower Bound Python
