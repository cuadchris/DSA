def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def findLargest(arr):
    largest = arr[0]
    largest_index = 0
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
            largest_index = i
    return largest_index


def selectionSort(arr, order='ascending'):
    res = []

    if order == 'descending':
        for i in range(len(arr)):
            result = findLargest(arr)
            res.append(arr.pop(result))
    else:
        for i in range(len(arr)):
            result = findSmallest(arr)
            res.append(arr.pop(result))
    return res


arr = [10, 9, 0, 11, 13, 1, 3, 7, 15, 2, 5, 6, 4, 8, 12, 14]

print(arr)
arr = selectionSort(arr)
print(arr)
arr = selectionSort(arr, 'descending')
print(arr)
