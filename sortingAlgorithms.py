import math
import random

def format_array(arr):
    n = len(arr)
    if n <= 10:
        return str(arr)
    else:
        # first and last 4 elements
        return str(arr[:4]) + ' ... ' + str(arr[-4:])
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
        iter[0] += 1
        A[k] = B[i]
        i += 1; k += 1
    # leftover from C
    while j < len(C):
        iter[0] += 1
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
        return -1, 0  # empty input
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
        key = arr[i]
        j = i - 1
        num_of_ops += 1
        while j >= 0 and arr[j] > key:
            num_of_ops += 2
            arr[j+1] = arr[j]
            j -= 1
        num_of_ops += 1

        arr[j+1] = key
        num_of_ops += 1
    return arr, num_of_ops


# finding the majority element after sorting
def find_majority_in_sorted(arr):

    n = len(arr)
    if n == 0:
        return -1, 0

    median_element = arr[(n-1)//2] # median position

    ver_num_of_ops = 0
    cnt = 0
    for x in arr:
        ver_num_of_ops += 1
        if x == median_element:
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
            num_of_ops += 1
        else:
            freq[i] = 1
            num_of_ops += 1

        num_of_ops += 1
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
        num_of_ops += 1
        if votes == 0:
            candidate = i
            num_of_ops += 1
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
            return left
        if right_count > majority_threshold:
            return right

        return -1

    majority = helper(0, len(arr) - 1)
    return majority, counter[0]

def majority_by_quick_sort(arr):
    counter = [0]
    if not arr:
        return -1, 0

    def quickSort(a, low, high):
        while low < high:
            # pivot is a[high]
            pivot = a[high]
            i = low - 1
            for j in range(low, high):
                counter[0] += 1
                if a[j] <= pivot:
                    i += 1
                    a[i], a[j] = a[j], a[i]
            a[i+1], a[high] = a[high], a[i+1]
            p = i+1

            # recurse on smaller side, loop on larger
            if p - low < high - p:
                quickSort(a, low, p-1)
                low = p+1
            else:
                quickSort(a, p+1, high)
                high = p-1

    a = arr.copy()
    quickSort(a, 0, len(a)-1)

    # median + verify
    n = len(a)
    cand = a[n//2]
    count = sum(1 for x in a if x == cand)
    counter[0] += n
    return (cand if count > n//2 else -1), counter[0]

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

        # ------------------------------------------------------------------
        # Extra test patterns to exercise best / worst cases of each algorithm
        # ------------------------------------------------------------------

        # 1. maj_first  – majority element appears at the very start (best for brute‑force)
        maj_first = [M1] * k + list(range(30 * n, 30 * n + (n - k)))
        fam['maj_first'] = maj_first

        # 2. maj_last   – majority element clustered at the end (worst for brute‑force)
        maj_last = list(range(40 * n, 40 * n + (n - k))) + [M1] * k
        fam['maj_last'] = maj_last

        # 3. median_pivot – array whose first element is the median value
        median_val = n // 2
        median_tail = [x for x in range(50 * n, 50 * n + n - 1)]
        random.shuffle(median_tail)
        median_pivot = [median_val] + median_tail
        fam['median_pivot'] = median_pivot

        # 4. single_value – explicit alias of the all‑same array
        fam['single_value'] = fam['all_same']

        # 5. all_distinct – explicit alias of the no‑majority / all‑unique case
        fam['all_distinct'] = fam['no_majority']

        catalog[n] = fam
    return catalog

if __name__ == '__main__':
    import sys
    with open("output.txt", "w") as f:
        sys.stdout = f

        sizes  = [8, 16, 32, 64, 128, 256, 512, 1024]
        catalog = generate_input_catalog(sizes)

        print("n    array                                                        | BruteForce  MergeSort  Insertion  Hashing  BoyerMoore  QuickSort  DivideConq")
        print("-"*147)
        for n in sizes:
            for fam_name, arr in catalog[n].items():
                brute_force_major,  brute_force_ops  = bruteForceMajority(arr.copy())
                merge_major,  merge_ops  = find_majority_by_merge(arr.copy())
                insertion_sort_major,  insertion_sort_ops  = find_majority_in_sorted(insertion_sort(arr.copy())[0])
                hash_major,  hash_ops  = hashing_based(arr.copy())
                boyer_major,  boyer_ops  = boyer_moore(arr.copy())
                quick_sort_major,  quick_sort_ops  = majority_by_quick_sort(arr.copy())
                div_conq_major,  div_conqt_ops  = find_majority_divide_and_conquer(arr.copy())

                print(f"{n:<4} {format_array(arr):<60} | "
                      f"{brute_force_ops:>10} {merge_ops:>10} {insertion_sort_ops:>10} {hash_ops:>10} "
                      f"{boyer_ops:>10} {quick_sort_ops:>10} {div_conqt_ops:>10}")
            print("-"*147)

        print("\nMajority elements found by each algorithm:")
        print("n    array                                                        | BruteForce  MergeSort  Insertion  Hashing  BoyerMoore  QuickSort  DivideConq")
        print("-"*147)
        for n in sizes:
            for fam_name, arr in catalog[n].items():
                brute_force_major, _  = bruteForceMajority(arr.copy())
                merge_major, _  = find_majority_by_merge(arr.copy())
                insertion_sort_major, _  = find_majority_in_sorted(insertion_sort(arr.copy())[0])
                hash_major, _  = hashing_based(arr.copy())
                boyer_major, _  = boyer_moore(arr.copy())
                quick_sort_major, _  = majority_by_quick_sort(arr.copy())
                div_conq_major, _  = find_majority_divide_and_conquer(arr.copy())


                print(f"{n:<4} {format_array(arr):<60} | "
                      f"{str(brute_force_major):>10} {str(merge_major):>10} {str(insertion_sort_major):>10} {str(hash_major):>10} "
                      f"{str(boyer_major):>10} {str(quick_sort_major):>10} {str(div_conq_major):>10}")
            print("-"*147)


