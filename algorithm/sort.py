import random
import time

def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        return func(*args, **kwargs), round(time.time() - start, 3)
    return wrapper

@timing
def bubble_sort(ls):
    for i in range(len(ls)):
        is_swapped = False
        for j in range(len(ls)-i-1):
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]
                is_swapped = True
        if not is_swapped:
            break
    return ls

@timing
def selection_sort(ls):
    for i in range(len(ls)):
        for j in range(i, len(ls)):
            if ls[i] > ls[j]:
                ls[i], ls[j] = ls[j], ls[i]
    return ls

@timing
def insertion_sort(ls):
    for i in range(1, len(ls)):
        temp = ls[i]
        j = i
        while j > 0 and temp < ls[j-1]:
            ls[j] = ls[j-1]
            j -= 1
        ls[j] = temp
    return ls

@timing
def shell_sort(ls):
    gap = len(ls) // 2
    while(gap > 0):
        for i in range(gap, len(ls)):
            temp = ls[i]
            j = i
            while j > 0 and temp < ls[j-gap]:
                ls[j] = ls[j-gap]
                j -= gap
            ls[j] = temp
        gap //= 2
    return ls


@timing
def merge_sort(ls):
    def sort(ls):
        if len(ls) <= 1:
            return ls
        ls_left = sort(ls[:len(ls)//2])
        ls_right = sort(ls[len(ls)//2:])

        l = r = m = 0
        while l < len(ls_left) and r < len(ls_right):
            if ls_left[l] < ls_right[r]:
                ls[m] = ls_left[l]
                l += 1
                m += 1
            else:
                ls[m] = ls_right[r]
                r += 1
                m += 1
        
        while l < len(ls_left):
            ls[m] = ls_left[l]
            l += 1
            m += 1
        
        while r < len(ls_right):
            ls[m] = ls_right[r]
            r += 1
            m += 1
        
        return ls
    return sort(ls)

@timing
def heap_sort(ls):
    def heapify_max(ls, n, i):
        while True:
            biggest = i
            l = 2 * i + 1
            r = 2 * i + 2

            biggest = l if l < n and ls[l] > ls[biggest] else biggest 
            biggest = r if r < n and ls[r] > ls[biggest] else biggest 

            if biggest != i:
                ls[i], ls[biggest] = ls[biggest], ls[i]
                i = biggest 
            else: break
        return

    for i in range(len(ls)//2-1, -1, -1):
        heapify_max(ls, len(ls), i)

    for n in range(len(ls)-1, 0, -1):
        ls[n], ls[0] = ls[0], ls[n]
        heapify_max(ls, n, 0)

    return ls

@timing
def quick_sort(ls):
    def sort(ls, start, end):
        pivot = end
        l = start
        r = pivot - 1
        if end - start <= 0:
            return
        ls[pivot], ls[(l+r)//2] = ls[(l+r)//2], ls[pivot] # worst-case O(N*N)을 피하고자 pivot 값을 중간값으로 사용
        while True:
            while l < end and ls[l] < ls[pivot]:
                l += 1
            while r > l and ls[r] > ls[pivot]:
                r -= 1
            if l < r:
                ls[l], ls[r] = ls[r], ls[l]
            else:
                break
        ls[l], ls[pivot] = ls[pivot], ls[l]
        sort(ls, start, l-1)
        sort(ls, l+1, end)
        return ls

    return sort(ls, 0, len(ls)-1)
        # return ((start, l-1), (l+1, end))
    
    # def run(ls):
    #     stack = [[0, len(ls)-1]]
    #     while stack:
    #         now = stack.pop()
    #         next = sort(ls, now[0], now[1])
    #         if next:
    #             stack.append(next[0])
    #             stack.append(next[1])
    #     return ls

    # return run(ls)

@timing
def counting_sort(ls):
    count_arr = [0 for _ in range(max(ls)+1)]
    for a in ls:
        count_arr[a] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]

    result = [0 for _ in range(len(ls))]
    for i in range(len(ls)-1, -1, -1):
        count_arr[ls[i]] -= 1
        result[count_arr[ls[i]]] = ls[i]

    return result

@timing
def radix_sort(ls):
    def counting_sort_for_radix(ls, digit):
        count_arr = [0 for _ in range(10)]
        for a in ls:
            count_arr[a//digit%10] += 1

        for i in range(1, len(count_arr)):
            count_arr[i] += count_arr[i-1]

        result = [0 for _ in range(len(ls))]
        for i in range(len(ls)-1, -1, -1):
            index = ls[i]//digit%10
            count_arr[index] -= 1
            result[count_arr[index]] = ls[i]

        ls[:] = result[:]
        return

    max_digit = 10**(len(str(max(ls)))-1)
    d = 1
    while d <= max_digit:
        counting_sort_for_radix(ls, d)
        d *= 10

    return ls

@timing
def python_sort(ls):
    return sorted(ls)

# ---

sorting_algorithms = {
    # "bubble_sort": bubble_sort,
    # "selection_sort": selection_sort,
    # "insertion_sort": insertion_sort,
    # "shell_sort": shell_sort,
    # "merge_sort": merge_sort,
    # "heap_sort": heap_sort,
    "quick_sort": quick_sort,
    # "counting_sort": counting_sort,
    # "radix_sort": radix_sort,
    # "python_sort(tim sort+CPython)": python_sort,
}

TEST_CASES_SIZE = 10**4
SAMPLE_LIST = [0, 1, 2, 2] + [i for i in range(3, TEST_CASES_SIZE-1)]

test_cases = {
    "best": [i for i in range(TEST_CASES_SIZE)],
    "worst": [i for i in reversed(range(TEST_CASES_SIZE))],
    "test1": random.sample(SAMPLE_LIST, len(SAMPLE_LIST)),
    "test2": random.sample(SAMPLE_LIST, len(SAMPLE_LIST)),
    "test3": random.sample(SAMPLE_LIST, len(SAMPLE_LIST)),
}

for name, func in sorting_algorithms.items():
    print(f"[ {name} ]")
    for test in test_cases:
        answer = func(test_cases[test][:])
        print(f"{test}: {test_cases[test][:10]} -> {answer[0][:10]}, time: {answer[1]}")
    print()
