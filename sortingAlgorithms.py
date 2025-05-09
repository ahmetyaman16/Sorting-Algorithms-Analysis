import math
import random

def format_array(arr):
    n = len(arr)
    if n <= 10:
        return str(arr)
    else:
        # show first 3 and last 3 elements
        return str(arr[:3]) + ' ... ' + str(arr[-3:])
def bruteForceMajority(A):
    n = len(A)
    iter = 0
    for i in range(n):
        count = 0
        for j in range(n):
            iter += 1
            if A[j] == A[i]:
                count += 1
        iter += 1
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
            num_of_ops += 1       # compare + shift
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key # Finding the majority element after sorting
def find_majority_in_sorted(arr):

    n = len(arr)
    if n == 0:
        return -1, 0

    median_element = arr[(n-1)//2] # pick median position

    iter = 0
    cnt = 0
    for x in arr:
        iter += 1
        if x == median_element:     # compare x == median_element
            cnt += 1
    iter += 1        # compare cnt > n/2

    if cnt > n//2:
        return median_element, iter
    else:
        return -1, iter

# Hashing‐based majority
def hashing_based(arr):
    freq = {}
    threshold = len(arr)//2
    iter = 0

    for i in arr:
        if i in freq:
            freq[i] += 1
            iter += 1
        else:
            freq[i] = 1
            iter += 1

        iter += 1           # compare freq[i] > threshold
        if freq[i] > threshold:
            return i, iter

    return -1, iter



# Boyer–Moore majority vote
def boyer_moore(arr):
    iter = 0
    votes = 0
    candidate = None

    # candidate selection
    for i in arr:
        iter += 1           # loop iteration
        if votes == 0:
            candidate = i
        iter += 1           # compare i == candidate
        votes += 1 if i == candidate else -1

    # verification
    actual = 0
    for i in arr:
        iter += 1           # compare i == candidate
        if i == candidate:
            actual += 1
    iter += 1               # final > test
    return (candidate if actual > len(arr)//2 else -1), iter

def find_majority_divide_and_conquer(arr):
    counter = [0]

    if not arr:
        return -1, 0

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

        left_count = right_count = 0
        for i in range(l, r + 1):
            counter[0] += 1
            if arr[i] == left:
                left_count += 1
            elif arr[i] == right:
                right_count += 1

        majority_threshold = (r - l + 1) // 2
        if left_count > majority_threshold:
            counter[0] += 1
            return left
        if right_count > majority_threshold:
            counter[0] += 1
            return right

        return -1

    majority = helper(0, len(arr) - 1)
    return majority, counter[0]


def majority_by_quick_sort(arr):
    counter = [0]

    if not arr:
        return -1, 0

    def quickSort(arr, low, high):
        if low < high:
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                counter[0] += 1
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            quickSort(arr, low, i)
            quickSort(arr, i + 2, high)

    arr = arr.copy()  # avoid modifying original
    quickSort(arr, 0, len(arr) - 1)

    candidate = arr[len(arr) // 2]
    count = sum(1 for x in arr if x == candidate)
    counter[0] += len(arr)

    if count > len(arr) // 2:
        return candidate, counter[0]
    return -1, counter[0]


def generate_input_catalog(sizes, swap_frac=0.05, heavy_frac=0.9, seed=0):
    random.seed(seed)
    catalog = {}
    for n in sizes:
        fam = {}
        # edge cases
        fam['empty']     = []
        fam['singleton'] = [0] if n>=1 else []
        # no majority
        fam['no_majority'] = list(range(n))
        # pick two “majority” symbols outside [0,n)
        M1, M2 = n+1, n+2
        # exact majority
        k = n//2 + 1
        rest = list(range(n, n + (n-k)))
        fam['with_majority'] = [M1]*k + rest
        random.shuffle(fam['with_majority'])
        # all same
        fam['all_same'] = [M1]*n
        # sorted
        asc = list(range(n))
        fam['sorted_asc']  = asc.copy()
        fam['sorted_desc'] = asc[::-1]
        # almost sorted
        a = asc.copy()
        swaps = max(1, int(n * swap_frac))
        for _ in range(swaps):
            i, j = random.randrange(n), random.randrange(n)
            a[i], a[j] = a[j], a[i]
        fam['almost_sorted'] = a
        # alternating
        fam['alternating'] = [(M2 if i%2==0 else i) for i in range(n)]
        # clustered
        fam['clustered'] = [M2]*k + list(range(n + (n-k), n + 2*(n-k)))
        # heavy hitter
        num_hh = int(n * heavy_frac)
        rest_hh = list(range(2*n, 2*n + (n - num_hh)))
        hh = [M2]*num_hh + rest_hh
        random.shuffle(hh)
        fam['heavy_hitter'] = hh
        # random families
        fam['random_no_majority'] = random.sample(range(3*n, 10*n), k=n)
        rm_rest = random.sample(range(10*n, 20*n), k=n-k)
        arr = [M1]*k + rm_rest
        random.shuffle(arr)
        fam['random_with_majority'] = arr

        catalog[n] = fam
    return catalog

# Simple driver over fixed tests
if __name__ == '__main__':
    sizes  = [10, 100, 500, 1000]
    catalog = generate_input_catalog(sizes)

    # Full-name header
    print("n    array                                         | BruteForce  MergeSort  Insertion  Hashing  BoyerMoore  QuickSort  DivideConq")
    print("-"*130)

    for n in sizes:
        for fam_name, arr in catalog[n].items():
            # run all seven
            bf_maj,  bf_ops  = bruteForceMajority(arr.copy())
            ms_maj,  ms_ops  = find_majority_by_merge(arr.copy())
            is_maj,  is_ops  = find_majority_in_sorted(insertion_sort(arr.copy())[0])
            hb_maj,  hb_ops  = hashing_based(arr.copy())
            bm_maj,  bm_ops  = boyer_moore(arr.copy())
            qs_maj,  qs_ops  = majority_by_quick_sort(arr.copy())
            dc_maj,  dc_ops  = find_majority_divide_and_conquer(arr.copy())

            # print a single row for all algorithms (ops only, as per header)
            print(f"{n:<4} {format_array(arr):<45} | "
                  f"{bf_ops:>10} {ms_ops:>10} {is_ops:>10} {hb_ops:>10} "
                  f"{bm_ops:>10} {qs_ops:>10} {dc_ops:>10}")
        print("-"*130)

    # ── Table: Majority elements per algorithm ───────────────────────────────
    print("\nMajority elements found by each algorithm:")
    print("n    array                                         | BruteForce  MergeSort  Insertion  Hashing  BoyerMoore  QuickSort  DivideConq")
    print("-"*130)
    for n in sizes:
        for fam_name, arr in catalog[n].items():
            bf_maj, _  = bruteForceMajority(arr.copy())
            ms_maj, _  = find_majority_by_merge(arr.copy())
            is_maj, _  = find_majority_in_sorted(insertion_sort(arr.copy())[0])
            hb_maj, _  = hashing_based(arr.copy())
            bm_maj, _  = boyer_moore(arr.copy())
            qs_maj, _  = majority_by_quick_sort(arr.copy())
            dc_maj, _  = find_majority_divide_and_conquer(arr.copy())

            print(f"{n:<4} {format_array(arr):<45} | "
                  f"{str(bf_maj):>10} {str(ms_maj):>10} {str(is_maj):>10} {str(hb_maj):>10} "
                  f"{str(bm_maj):>10} {str(qs_maj):>10} {str(dc_maj):>10}")
        print("-"*130)

    # ── Table: Majority elements per algorithm ───────────────────────────────
    print("\nMajority elements found by each algorithm:")
    print("n    array                                         | BruteForce  MergeSort  Insertion  Hashing  BoyerMoore  QuickSort  DivideConq")
    print("-"*130)
    for n in sizes:
        for fam_name, arr in catalog[n].items():
            bf_maj, _  = bruteForceMajority(arr.copy())
            ms_maj, _  = find_majority_by_merge(arr.copy())
            is_maj, _  = find_majority_in_sorted(insertion_sort(arr.copy())[0])
            hb_maj, _  = hashing_based(arr.copy())
            bm_maj, _  = boyer_moore(arr.copy())
            qs_maj, _  = majority_by_quick_sort(arr.copy())
            dc_maj, _  = find_majority_divide_and_conquer(arr.copy())

            print(f"{n:<4} {format_array(arr):<45} | "
                  f"{str(bf_maj):>10} {str(ms_maj):>10} {str(is_maj):>10} {str(hb_maj):>10} "
                  f"{str(bm_maj):>10} {str(qs_maj):>10} {str(dc_maj):>10}")
        print("-"*130)
