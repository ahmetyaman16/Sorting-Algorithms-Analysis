import math

def find_majority_divide_and_conquer(arr, counter):
    counter=[0]
    
    def helper(l, r):
        if l == r:
            counter[0] += 1
            return arr[l]

        m = (l + r) // 2
        left = helper(l, m)
        right = helper(m + 1, r)

        if left == right:
            counter[0] += 1
            return left

        left_count = 0
        right_count = 0
        for i in range(l, r + 1):
            counter[0] += 1
            if arr[i] == left:
                left_count += 1
            elif arr[i] == right:
                right_count += 1

        majority_threshold = (r - l + 1) // 2
        if left_count > majority_threshold:
            return left
        if right_count > majority_threshold:
            return right

        return -1

    if not arr:
        return -1

    return helper(0, len(arr) - 1)
def quickSort(arr, low, high, counter):
    if low < high:
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            counter[0] += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        quickSort(arr, low, i, counter)
        quickSort(arr, i + 2, high, counter)

def majority_by_sort(arr, counter):
    conter=[0]
    if not arr:
        return -1

    quickSort(arr, 0, len(arr) - 1, counter)

    candidate = arr[len(arr) // 2]
    count = sum(1 for x in arr if x == candidate)
    counter[0] += len(arr)

    if count > len(arr) // 2:
        return candidate
    return -1

