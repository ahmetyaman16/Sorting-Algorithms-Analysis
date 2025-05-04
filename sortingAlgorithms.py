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
            print("Number of iterations:", iter)
            return A[i]
    print("Number of iterations:", iter)   
    return -1

#Examples:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("The majority element is:", bruteForceMajority(arr))
arr2 = [1, 2, 8, 8, 5, 8, 7, 8, 9, 10]
print("The majority element is:", bruteForceMajority(arr2))
arr3 = [2, 3, 3, 3, 3, 6, 7, 3, 9, 3, 3, 1]
print("The majority element is:", bruteForceMajority(arr3))


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

def findMajority(A):
    iter = [0]
    mergeSortMajority(A,iter)
    total_iters = iter[0]
    n=len(A)
    candidate = A[math.floor(len(A)/2)]
    if A.count(candidate) > math.floor(len(A)/2):
        return candidate,total_iters
    else:
        return -1,total_iters


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("The majority element is:", findMajority(arr))
arr2 = [1, 2, 8, 8, 5, 8, 7, 8, 9, 10]
print("The majority element is:", findMajority(arr2))
arr3 = [3, 2, 3, 3, 3, 6, 7, 3, 9, 3, 3, 1]
print("The majority element is:", findMajority(arr3))