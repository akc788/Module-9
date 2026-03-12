import random
import time

#data structure with at least 300 elements
data = [random.randint(1, 1000) for _ in range(300)]

#Selection Sort
def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


#Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


#Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


#Performance Testing

# Selection Sort
start = time.time()
sorted_selection = selection_sort(data)
end = time.time()
print("Selection Sort Time:", end - start)
print("Selection Sorted Data:", sorted_selection)


# Merge Sort
start = time.time()
sorted_merge = merge_sort(data)
end = time.time()
print("\nMerge Sort Time:", end - start)
print("Merge Sorted Data:", sorted_merge)


# Quick Sort
start = time.time()
sorted_quick = quick_sort(data)
end = time.time()
print("\nQuick Sort Time:", end - start)
print("Quick Sorted Data:", sorted_quick)