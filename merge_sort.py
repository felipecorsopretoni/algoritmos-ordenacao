import random
import time
import math

moves = 0

def merge_sort(arr):
    global moves
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    global moves
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        moves += 1
    while i < len(left):
        result.append(left[i])
        i += 1
        moves += 1
    while j < len(right):
        result.append(right[j])
        j += 1
        moves += 1
    return result

random.seed(42)
sizes = [1000, 10000, 100000]

for size in sizes:
    arr = [random.randint(1, 1000000) for _ in range(size)]
    times = []
    ops = 0
    for _ in range(3):
        moves = 0
        a = arr[:]
        t0 = time.perf_counter()
        merge_sort(a)
        t1 = time.perf_counter()
        ops = moves
        times.append(round(t1 - t0, 6))
    avg = sum(times) / 3
    std = math.sqrt(sum((t - avg) ** 2 for t in times) / 3)
    print(f"n={size} | tempos={times} | media={avg:.6f}s | std={std:.6f} | movimentacoes={ops}")