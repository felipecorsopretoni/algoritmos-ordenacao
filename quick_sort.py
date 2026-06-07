import random
import time
import math
import sys

sys.setrecursionlimit(200000)

swaps = 0

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    global swaps
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    swaps += 1
    return i + 1

random.seed(42)
sizes = [1000, 10000, 100000]

for size in sizes:
    arr = [random.randint(1, 1000000) for _ in range(size)]
    times = []
    ops = 0
    for _ in range(3):
        swaps = 0
        a = arr[:]
        t0 = time.perf_counter()
        quick_sort(a, 0, len(a) - 1)
        t1 = time.perf_counter()
        ops = swaps
        times.append(round(t1 - t0, 6))
    avg = sum(times) / 3
    std = math.sqrt(sum((t - avg) ** 2 for t in times) / 3)
    print(f"n={size} | tempos={times} | media={avg:.6f}s | std={std:.6f} | trocas={ops}")