import random
import time
import math

def insertion_sort(arr):
    moves = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            moves += 1
        arr[j + 1] = key
    return moves

random.seed(42)
sizes = [1000, 10000, 100000]

for size in sizes:
    arr = [random.randint(1, 1000000) for _ in range(size)]
    times = []
    ops = 0
    for _ in range(3):
        a = arr[:]
        t0 = time.perf_counter()
        ops = insertion_sort(a)
        t1 = time.perf_counter()
        times.append(round(t1 - t0, 6))
    avg = sum(times) / 3
    std = math.sqrt(sum((t - avg) ** 2 for t in times) / 3)
    print(f"n={size} | tempos={times} | media={avg:.6f}s | std={std:.6f} | movimentacoes={ops}")