def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

example = [64, 28, 21, 18, 63, 14, 81]
print(quick_sort(example))  # [14, 18, 21, 28, 63, 64, 81]