import math

def bruteForceMajority(A):
    n = len(A)
    iter = 0
    for i in range(n):
        count = 0
        for j in range(n):
            iter += 1
            if A[j] == A[i]:
                count += 1
        if count > math.floor(n / 2):
           # print("Number of iterations:", iter)
            return A[i], iter
   # print("Number of iterations:", iter)
    return -1, iter


def merge(B, C, A, iter):
    i=0
    j=0
    k=0
    while i<len(B) and j<len(C):
        iter[0] += 1
        if B[i] < C[j]:
            A[k] = B[i]
            i += 1
        else:
            A[k] = C[j]
            j += 1
        k += 1
     # leftover from B
    while i < len(B):
        iter[0] += 1              # ← and here
        A[k] = B[i]
        i += 1; k += 1
    # leftover from C
    while j < len(C):
        iter[0] += 1              # ← and here
        A[k] = C[j]
        j += 1; k += 1

def mergeSortMajority(A, iter):
    B = []
    C = []
    n = len(A)
    mid = math.floor(n/2)
    if n > 1:
        B = A[:mid]
        C = A[mid:]
        mergeSortMajority(B,iter)
        mergeSortMajority(C,iter)
        merge(B, C, A, iter)
    return A


def find_majority_by_merge(A):
    if len(A) == 0:
        return -1, 0  # No operations, empty input
    iter = [0]
    mergeSortMajority(A, iter)
    total_iters = iter[0]
    n = len(A)
    candidate = A[n // 2]
    if A.count(candidate) > n // 2:
        return candidate, total_iters
    else:
        return -1, total_iters



# Insertion‐sort
def insertion_sort(arr):
    num_of_ops = 0
    for i in range(1, len(arr)):
        key = arr[i]               # assignment of key & j
        j = i - 1
        num_of_ops += 1
        while j >= 0 and arr[j] > key:
            num_of_ops += 2       # compare + shift
            arr[j+1] = arr[j]
            j -= 1
        num_of_ops += 1           # final failed compare

        arr[j+1] = key
        num_of_ops += 1           # assignment
    return arr, num_of_ops


# Finding the majority element after sorting
def find_majority_in_sorted(arr):

    n = len(arr)
    if n == 0:
        return -1, 0

    median_element = arr[(n-1)//2] # pick median position

    ver_num_of_ops = 0
    cnt = 0
    for x in arr:
        ver_num_of_ops += 1
        if x == median_element:     # compare x == median_element
            cnt += 1
    ver_num_of_ops += 1

    return (median_element if cnt > n//2 else -1),ver_num_of_ops # final > n//2 test


# Hashing‐based majority
def hashing_based(arr):
    freq = {}
    threshold = len(arr)//2
    num_of_ops = 0

    for i in arr:
        if i in freq:
            freq[i] += 1
            num_of_ops += 1       # update
        else:
            freq[i] = 1
            num_of_ops += 1       # insertion

        num_of_ops += 1           # compare freq[i] > threshold
        if freq[i] > threshold:
            return i, num_of_ops

    return -1, num_of_ops


# Boyer–Moore majority vote
def boyer_moore(arr):
    num_of_ops = 0
    votes = 0
    candidate = None

    # candidate selection
    for i in arr:
        num_of_ops += 1           # loop iteration
        if votes == 0:
            candidate = i
            num_of_ops += 1       # assignment
        num_of_ops += 1           # compare i == candidate
        votes += 1 if i == candidate else -1

    # verification
    actual = 0
    for i in arr:
        num_of_ops += 1           # compare i == candidate
        if i == candidate:
            actual += 1

    num_of_ops += 1               # final > test
    return (candidate if actual > len(arr)//2 else -1), num_of_ops


# Simple driver over fixed tests
if __name__ == '__main__':
    tests = [
        [],
        [42],
        [1, 2],
        [3, 3],
        [1, 2, 3, 4, 5, 6],
        [9, 9, 9, 1, 2, 3, 4],
        [7, 7, 7, 7, 7, 7],
        [5, 1, 5, 2, 5, 3, 5],
        [8, 8, 8, 8, 1, 2, 3],
        [4, 4, 4, 4, 4, 1, 2],
    ]


    print(f"------------------------------------------------------------------------")
    for arr in tests:

        sorted_arr, sort_ops = insertion_sort(arr.copy())
        major_insertion, ver_ops = find_majority_in_sorted(sorted_arr)
        total_ops = sort_ops + ver_ops

        major_hash, num_of_ops_hash   = hashing_based(arr)
        major_boyer,   num_of_ops_bm     = boyer_moore(arr)
        major_brute_force, num_of_ops_brute  = bruteForceMajority(arr)
        major_merge, num_of_ops_merge        =  find_majority_by_merge(arr)

        print("Input: ", arr)
        print("Method          | Majority element | Number of basic operation")
        print(f"Insertion sort  | {major_insertion:3}              |  {total_ops}")
        print(f"Hashing         | {major_hash:3}              |  {num_of_ops_hash}")
        print(f"Boyer–Moore     | {major_boyer:3}              |  {num_of_ops_bm}")
        print(f"Brute Force     | {major_brute_force:3}              |  {num_of_ops_brute}")
        print(f"Merge sort     | {major_merge:3}              |  {num_of_ops_merge}")
        print(f"------------------------------------------------------------------------")
        print()