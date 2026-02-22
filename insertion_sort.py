def insertion_sort(arr):
    for i in range(1, len(arr)):
        pos = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > pos:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = pos
    return arr

example = [56, 47, 456, 4, 89, 110, 15]
print(insertion_sort(example)) # [4, 15, 47, 56, 89, 110, 456]