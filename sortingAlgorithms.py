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
