import bisect

def binary_search_with_bisect(arr, target):
    i = bisect.bisect_left(arr, target)
    if i != len(arr) and arr[i] == target:
        return i
    return -1

sorted_example = [11, 12, 22, 25, 34, 64, 90]
target = 34
result = binary_search_with_bisect(sorted_example, target)
print(f"Элемент {target} найден на позиции {result}" if result != -1 else f"Элемент {target} не найден")